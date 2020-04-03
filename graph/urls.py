from django.conf.urls import url

from . import views
from .views import graph,returnjson,sendjson

urlpatterns = [
    url(r'^$', graph),
    url(r'^json/returnjson$', views.returnjson, name='returnjson'),
    url(r'^json/sendjson$', views.sendjson, name='sendjson'),
]