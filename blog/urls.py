from django.conf.urls import url
from . import views
from django.urls import path
from django.urls import include
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^lekarz/$', views.lekarz_list, name='lekarz_list'),
    url(r'^galeria/$', views.galeria, name='galeria'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^lekarz/(?P<pk>[0-9]+)/$', views.lekarz_detail, name='lekarz_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^lekarz/new/$', views.lekarz_new, name='lekarz_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^lekarz/(?P<pk>[0-9]+)/edit/$', views.lekarz_edit, name='lekarz_edit'),
]