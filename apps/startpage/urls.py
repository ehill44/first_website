from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^process1$', views.process1, name='post1'),
    url(r'^process2$', views.process2, name='post2'),
]