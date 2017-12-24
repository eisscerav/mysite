# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)


