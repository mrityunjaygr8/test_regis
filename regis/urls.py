from django.conf.urls import url,include
from regis import views
import regbackend

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^accounts/profile/',views.profile,name = "profile"),
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view(), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
