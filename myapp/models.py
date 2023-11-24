from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    svgPath = models.CharField(max_length=800)
    iElementClass = models.CharField(max_length=100)
    iconColor = models.CharField(max_length=100)
