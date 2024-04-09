from django.shortcuts import render  # , redirect, get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout, authenticate
# from django.db import IntegrityError
# from .forms import TaskForm
# from .models import Task
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required

# Create your views here.


def business(request):
    return render(request, 'business.html')
