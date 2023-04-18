from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your models here.
class Review(models.Model):
    author = models.CharField(max_length = 256)
    product_name = models.CharField(max_length = 256)
    product_rating = models.IntegerField(max_length=10)
    product_review = models.CharField(max_length=256)
    date_submitted = models.DateTimeField(default = timezone.now)

    def str(self):
            return self.author.username

    def get_absolute_url(self):
            return reverse('review-detail', kwargs={'pk': self.pk})
    

class Product(models.Model):
    product_name = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    avg_cost = models.FloatField()
    category = models.CharField(max_length=256)
    date_released = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='product_pics')


    def __str__ (self):
        return self.product_name


    def get_absolute_url(self):
        return reverse('review-detail', kwargs = {'pk': self.pk})
    
   

    