from django.conf.urls import url,include
from regis import views
import regbackend

urlpatterns = [
    url(r'^$', views.index, name = "index"),
]
