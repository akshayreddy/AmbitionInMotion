"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from blog.views import PostAnswers, UserAnswers

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^calender/$',views.calender, name='calender'),
    url(r'^forum/$',views.forum, name='forum'),
    url(r'^post_questions/$',views.post_question, name='post_question'),
    #url(r'^post_answers/(?P<current_pk>\d+)/',UserAnswers.as_view(), name='post_answers'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^profile_edit/$',views.profile_edit, name='profile_edit'),
    url(r'^appointment/$',views.appointment_page, name='appointment'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^answer/(?P<pk>\d+)/', PostAnswers.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

