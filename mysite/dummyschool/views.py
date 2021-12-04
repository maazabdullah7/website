from django.shortcuts import render, redirect
from .models import Data

def index(request):
    return render(request, 'index.html')

def faculty(request):
    return render(request, 'faculty.html')

def contact(request):

    if request.method == 'POST':
        data = Data(
            name = request.POST['name'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        data.save()
        return redirect('index.html')
    return render(request, 'contact.html')
