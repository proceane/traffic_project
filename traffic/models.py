from django.db import models

# Create your models here.
class Traffic(models.Model):
    item1 = models.CharField(max_length=200)
    item2 = models.DateTimeField('item2')

