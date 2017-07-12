from django.db import models
from time import time

# Create your models here.


def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)



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



#python manage.py makemigrations
#python manage.py migrate