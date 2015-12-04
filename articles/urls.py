from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^detail/([0-9]+)/$', views.detail, name='detail'),
    url(r'^index/$', views.index, name='index'),
]