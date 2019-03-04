from django import forms
from .models import FoodModel



# form for model
class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodModel
        exclude = ["foodForeignKey"]