from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^scan/$', views.Scan.as_view(), name='scan'),
]
