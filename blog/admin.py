from django.contrib import admin

# Register your models here.

from .models import ProfileInfo
from .models import Appointments
from .models import Forum

admin.site.register(ProfileInfo)
admin.site.register(Appointments)
admin.site.register(Forum)
