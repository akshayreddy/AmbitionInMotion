

from django import forms
from .models import ProfileInfo, Appointments, Forum, ForumAnswers


class ProfileInfoForm(forms.ModelForm):
	class Meta:
		model = ProfileInfo
		fields = ['full_name', 'public_email', 'bio','url','location','thumbnail']

class AppointmentsForm(forms.ModelForm):
 	class Meta:
 		model = Appointments
 		fields = ['title','start','end','color']

class ForumForm(forms.ModelForm):
 	class Meta:
 		model = Forum
 		fields = ['question']		         # Add number of fields required
 		exclude = ['created_by']


class ForumAnswerForm(forms.ModelForm):
	class Meta:
		model = ForumAnswers
		fields = ['answer','question_id']                  # Add number of fields required
		exclude = ['created_by']