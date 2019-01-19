from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^process/$', views.Process.as_view(), name='process_data'),
]
