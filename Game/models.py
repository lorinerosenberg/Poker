# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')
    chips = models.IntegerField(default=0)
    profile_pic_url = models.CharField(max_length=800, default='')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)