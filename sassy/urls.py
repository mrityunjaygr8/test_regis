from django.conf.urls import url,include
from sassy import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
]
