from django.conf.urls import url
from . import views
from django.urls import path
from django.urls import include
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]