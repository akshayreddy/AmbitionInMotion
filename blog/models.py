from django.db import models
from time import time
from django.core.validators import URLValidator


# Create your models here.


class ProfileInfo(models.Model):
	full_name= models.CharField(max_length=50, blank=True, null=True)
	public_email= models.EmailField()
	bio= models.CharField(max_length=300, blank=True, null=True)
	url= models.CharField(max_length=300, blank=True, null=True)
	location= models.CharField(max_length=300, blank=True, null=True)
	timestamp= models.DateTimeField(auto_now_add=False, auto_now=True)
	thumbnail = models.FileField(upload_to="profile_image", blank=True)


	def __str__(self):
		return self.full_name


class Appointments(models.Model):

	title= models.CharField(max_length=50, blank=True, null=True)
	start= models.DateField()
	end= models.DateField()
	#url= models.TextField(validators=[URLValidator()], null=True)
	color = models.CharField(max_length=10, default="blue", null=False)

	def __str__(self):
		return self.title



class Forum(models.Model):

	question=models.CharField(max_length=500, blank=False, null=False)
	image= models.URLField(max_length=500, blank=True,verbose_name="Image URL")
	created= models.DateTimeField(auto_now_add=True)
	created_by= models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return "Q no. " +str(self.id)+" "+str(self.question)+ " posted by " +str(self.created_by)

	class Meta:
		ordering = ('-created',)



class ForumAnswers(models.Model):
	answer= models.CharField(max_length=1000, blank=False, null=False)
	image= models.URLField(max_length=500, blank=True,verbose_name="Image URL")
	url= models.URLField(max_length=500, blank=True,verbose_name="URL")
	created= models.DateTimeField(auto_now_add=True)
	answered_by= models.CharField(max_length=50, blank=True, null=True)
	question_id=models.ForeignKey(Forum, related_name="answers")

	def __str__(self):
		return str(self.answered_by) + " answered " + str(self.question_id)

	class Meta:
		ordering = ('-created',)


#python manage.py makemigrations
#python manage.py migrate