from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class board(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=50, default='No Name')
    author = models.CharField(max_length=50, default= 'Anonymous')
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default = 'None')

class nlist(models.Model):
    parent = models.ForeignKey(board, on_delete = models.CASCADE)
    list_name = models.CharField(max_length=30)

class card(models.Model):
    title = models.CharField(max_length=30)
    dad = models.IntegerField()

