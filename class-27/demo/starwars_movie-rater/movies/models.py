from django.db import models
from django.contrib.auth import get_user_model

class Movie(models.Model):
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=10)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name