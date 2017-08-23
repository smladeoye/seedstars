from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Jobs(models.Model):
    name = models.CharField(max_length=50)
    build_number = models.IntegerField(max_length=10)
    status = models.CharField(max_length=10)
    checked_time = models.DateTimeField()
