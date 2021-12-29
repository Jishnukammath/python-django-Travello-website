from django.db import models
from django.db.models.base import Model

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    discription=models.TextField()
    img=models.ImageField(upload_to="pictures")
    offer=models.BooleanField(default=False)

