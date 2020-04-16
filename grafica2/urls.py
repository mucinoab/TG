from django.conf.urls import url

from . import views
from .views import grafica2

urlpatterns = [
    url(r'^$', grafica2),
    url(r'^grafica2/json/returnjson$', views.returnjson, name='returnjson'),
    url(r'^grafica2/json/sendjson$', views.sendjson, name='sendjson'),
]
