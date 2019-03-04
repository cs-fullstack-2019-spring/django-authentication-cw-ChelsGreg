from django.shortcuts import render
from django.http import HttpResponse
from .forms import FoodModel, FoodForm
from django.contrib.auth.models import User


# Create your views here.

# HOME PAGE
def index(request):
    return render(request, 'foodApp/index.html')

# TO CREATE NEW CALORIE TRACKER
def newTrack(request):
    newForm = FoodForm(request.POST or None)
    context = {
        "newForm": newForm
    }

    return render(request, 'foodApp/newTrack.html', context)

# TO CREATE NEW USER
def loginhere(request):
    # newForm = FoodForm(request.POST or None)
    # context = {
    #     "newForm": newForm
    # }
    # if request.method == "POST":
    #     print(request.POST)
        User.objects.create_user(request.POST["username"], "", request.POST[""])

    return render(request, 'foodApp'/'loginhere.html', context)