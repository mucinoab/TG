from django.conf.urls import url

from . import views
from .views import index

urlpatterns = [
    url(r'^$', index),
]
