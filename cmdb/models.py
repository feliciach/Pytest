# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class queryLog(models.Model):
    ip=models.CharField(max_length=32)
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    add=models.CharField(max_length=64,null=True)
