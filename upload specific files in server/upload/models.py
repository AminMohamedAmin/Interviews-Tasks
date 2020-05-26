from django.db import models
from django.contrib.auth.models import User

class file(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    job=models.CharField(max_length=150)
    level=models.IntegerField(default=0)
    file=models.FileField(upload_to="media")
