

from django import forms
from .models import ProfileInfo


class ProfileInfoForm(forms.ModelForm):
	class Meta:
		model = ProfileInfo
		fields = ['full_name', 'public_email', 'bio','url','location','thumbnail']