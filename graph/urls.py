from django.conf.urls import url

from . import views
from .views import graph,returnjson

urlpatterns = [
    url(r'^$', graph),
    url(r'^json/returnjson$', views.returnjson, name='returnjson'),
]