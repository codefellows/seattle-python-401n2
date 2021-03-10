from django.contrib.auth import get_user_model
from django.db import models

class Snack(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name
