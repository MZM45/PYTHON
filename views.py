# myapp/views.py
from django.shortcuts import render

def index(request):
    message = "Welcome to Django! This message is coming from the backend."
    return render(request, 'index.html', {'message': message})
