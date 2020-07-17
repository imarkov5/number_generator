from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)
    guess = models.IntegerField()
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

