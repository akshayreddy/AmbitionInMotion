from django.contrib import admin

# Register your models here.

from .models import ProfileInfo, Appointments, Forum, ForumAnswers

admin.site.register(ProfileInfo)
admin.site.register(Appointments)
admin.site.register(Forum)
admin.site.register(ForumAnswers)
