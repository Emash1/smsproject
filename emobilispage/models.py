from django.db import models

class Emobilispage(models.Model):
    studfname = models.CharField(max_length=100)
    studlname = models.CharField(max_length=100)
    studemail = models.EmailField(unique=True,blank=True)
    studcourse = models.CharField(max_length=100)