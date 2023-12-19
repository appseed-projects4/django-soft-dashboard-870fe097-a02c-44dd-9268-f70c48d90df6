# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first name = models.CharField(max_length=255, null=True, blank=True)
    last name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    marital status = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Attendancerecord(models.Model):

    #__Attendancerecord_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    #__Attendancerecord_FIELDS__END

    class Meta:
        verbose_name        = _("Attendancerecord")
        verbose_name_plural = _("Attendancerecord")



#__MODELS__END
