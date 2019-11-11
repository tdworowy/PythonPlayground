from django.conf.urls import url

from dlinks import views

urlpatterns = [

url(r'^$', views.post_skype_data, name='post_SkypeDat'),     ]