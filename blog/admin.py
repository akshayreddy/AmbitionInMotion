from django.contrib import admin

# Register your models here.

from .models import ProfileInfo
from .models import Appointments

admin.site.register(ProfileInfo)
admin.site.register(Appointments)
