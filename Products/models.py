from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True)
    cost = models.IntegerField()
    description = models.TextField()
    inventory_in_hand = models.IntegerField()