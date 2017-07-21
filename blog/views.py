from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import ProfileInfo, Appointments
import time, datetime

# Create your views here.

from .forms import ProfileInfoForm, AppointmentsForm

def home(request):
	users = User.objects.all()
	print(users)
	return render(request, "home.html", {})

def calender(request):
	all_events= Appointments.objects.all()

	context ={
	"events": all_events,
	"curr_date": datetime.datetime.today().strftime('%Y-%m-%d'),
	}

	return render(request, "calender.html", context)

def profile(request):

	queryset = ProfileInfo.objects.all()

	for obj in queryset:
		instance = {"name":"","public_email":"","bio":"","url":"","location":""}
		instance["name"]=obj.full_name
		instance["public_email"]=obj.public_email
		instance["bio"]=obj.bio
		instance["url"]=obj.url
		instance["location"]=obj.location
		instance["thumbnail"]=obj.thumbnail

	context={
	   "instance":instance,

	}
	return render(request, "profile.html", context)

def profile_edit(request):

	form = ProfileInfoForm(request.POST, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
	   "form":form,
	}
	return render(request, "profile_edit.html", context)



def appointment_page(request):

	form = AppointmentsForm(request.POST, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
	"form" : form,
	}

	return render(request, "appointment.html", context)

