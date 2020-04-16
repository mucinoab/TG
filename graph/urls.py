from django.conf.urls import url

from . import views
from .views import graph

urlpatterns = [
    url(r'^$', graph),
    url(r'^graph/json/returnjson$', views.returnjson, name='returnjson'),
    url(r'^graph/json/sendjson$', views.sendjson, name='sendjson'),
]
