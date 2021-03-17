from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Movie(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
    