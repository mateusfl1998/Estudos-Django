from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    user_form = UserCreationForm
    return render(request, 'register.html', {'user_form': user_form})