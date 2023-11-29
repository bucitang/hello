from django.db import models

# Create your models here.
class zanghua(models.Model):
    kaipen = models.charField(max_lenth=64)
