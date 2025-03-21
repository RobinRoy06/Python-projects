from django.db import models
from django.core.validators import *
from datetime import date
# Create your models here.

class Game(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)],
        )
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    post_creation = models.DateField(default=date.today)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    ) 
    
    
    def __str__(self):
        return self.title
    
class Account(models.Model):
    username = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(4)]
    )
    password = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(8)]
    )
