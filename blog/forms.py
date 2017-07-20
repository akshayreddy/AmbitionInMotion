

from django import forms
from .models import ProfileInfo
from .models import Appointments


class ProfileInfoForm(forms.ModelForm):
	class Meta:
		model = ProfileInfo
		fields = ['full_name', 'public_email', 'bio','url','location','thumbnail']

class AppointmentsForm(forms.ModelForm):
 	class Meta:
 		model = Appointments
 		fields = ['title','start','end','color']



