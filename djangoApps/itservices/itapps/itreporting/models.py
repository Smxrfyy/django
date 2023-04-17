from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class review(models.Model):
    type = models.CharField(max_length = 256)
    room = models.CharField(max_length = 256)
    details = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_submitted = models.DateTimeField(default = timezone.now)
    

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('review-detail', kwargs = {'pk': self.pk})