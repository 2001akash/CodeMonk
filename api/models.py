# api/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dob = models.DateField(null=True, blank=True)

class Paragraph(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Word(models.Model):
    value = models.CharField(max_length=100)
    paragraph = models.ForeignKey(Paragraph, related_name='words', on_delete=models.CASCADE)