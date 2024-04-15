from django.db import models

class Emobilispage(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    coursename = models.CharField(max_length=100)