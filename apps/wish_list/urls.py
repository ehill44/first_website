from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^dashboard$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^process1$', views.process1, name='process1'),
    url(r'^process2$', views.process2, name='process2'),
    url(r'^process3$', views.process3, name='process3'),
    url(r'^process4$', views.process4, name='process4'),
    url(r'^(?P<id>\d+)$', views.show, name='show'),
]