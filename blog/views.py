from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import ProfileInfo, Appointments, Forum
import time, datetime

# Create your views here.

from .forms import ProfileInfoForm, AppointmentsForm, ForumForm

def home(request):
	users = User.objects.all()
	print(users)
	return render(request, "home.html", {})

def forum(request):

	all_events=Forum.objects.all()

	context = {
	"questions": all_events,

	}
	return render(request, "forum.html", context)

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

def post_question(request):

	form = ForumForm(request.POST, request.FILES or None)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.created_by = request.user
		instance.save()

	context = {
	   "form":form,
	}
	return render(request, "post_question.html", context)

