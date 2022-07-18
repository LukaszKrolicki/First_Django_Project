from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)  # field that contain text data
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)  # standard length for urls


class Offer(models.Model):
    code= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()