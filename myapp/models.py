from django.db import models

# Create your models here.
class Feature:
    id: int
    name: str
    details: str
    svgPath: str
    iElementClass: str
    iconColor: str
