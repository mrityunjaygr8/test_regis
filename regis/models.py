from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
  user = models.OneToOneField(User)

  phone = models.CharField(max_length = 64, default=0)

  first_name = models.CharField(max_length=64, default = '')
  last_name = models.CharField(max_length=64, default = '')

  def __unicode__(self):
  	return self.user.username

  def get_name(self):
  	return self.first_name+" "+self.last_name
  	