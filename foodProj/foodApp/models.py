from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Food model for username, calories, date
class FoodModel(models.Model):
    username = models.CharField(max_length=100, default="")
    calories = models.IntegerField(default=0)
    date = models.DateField()
    foodForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'