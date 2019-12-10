from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

class ViewsCount(models.Model):
    count = models.IntegerField(default=0,blank=True,null=True)
