import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    title=models.CharField(max_length=100)
    content=models.TextField()
    def get_absolute_url(self):
        return reverse('detailpost',kwargs={'pk':self.pk})