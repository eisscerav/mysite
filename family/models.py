# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    age = models.IntegerField(default=10, verbose_name='Age')
    gender = models.CharField(max_length=20, choices=(('M', 'Male'), ('F', 'Female')), verbose_name='Gender')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User Info'
        verbose_name_plural = verbose_name


class VisitHospital(models.Model):
    hospital = models.CharField(max_length=50, verbose_name='Hospital')
    pathogenesis = models.TextField(null=True, verbose_name='Pathogenesis')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    date = models.DateField(verbose_name='Date')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Visit Hospital Record'
        verbose_name_plural = verbose_name

