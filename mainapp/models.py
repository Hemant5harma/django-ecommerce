from django.db import models

# Create your models here.
CATERORY_CHOICES=[
    {'Men',"men"},
    {'Women','women'},
    {'Kids','kids'},
    {'Features','featured'},
    {'Latest','latest'}
]


class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    size=models.CharField(max_length=20)
    cateogry=models.CharField(max_length=20,choices=CATERORY_CHOICES)
    image=models.ImageField(upload_to='media')