from django.shortcuts import render, get_object_or_404
from .models import ProfileInfo

# Create your views here.

from .forms import ProfileInfoForm

def home(request):

	name="%s" % (request.user)
	context={
	   "user_name": name,

	}
	return render(request, "home.html", context)

def calender(request):

	name="%s" % (request.user)
	context={
	   "user_name": name,

	}
	return render(request, "calender.html", context)

def profile(request):

	#instance = get_object_or_404(ProfileInfo, full_name="priya")
	#print(instance.url)

	queryset = ProfileInfo.objects.all()

	for obj in queryset:
		instance = {"name":"","public_email":"","bio":"","url":"","location":""}
		instance["name"]=obj.full_name
		instance["public_email"]=obj.public_email
		instance["bio"]=obj.bio
		instance["url"]=obj.url
		instance["location"]=obj.location
		instance["thumbnail"]=obj.thumbnail

	print(instance)

	name="%s" % (request.user)
	given_name="Batman"
	email="batman@gotham.com"
	bio="I Am The Batman. Iron-Man Sucks"
	url="https://github.com/akshayreddy"
	location="Bloomington, Indiana, USA"

	context={
	   "user_name": name,
	   "name": given_name,
	   "email":email,
	   "bio":bio,
	   "url":url,
	   "location":location,
	   "instance":instance,

	}
	return render(request, "profile.html", context)

def profile_edit(request):

	name="%s" % (request.user)
	form = ProfileInfoForm(request.POST, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
	   "form":form,
	   "user_name": name,

	}
	return render(request, "profile_edit.html", context)