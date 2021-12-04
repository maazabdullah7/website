from django.shortcuts import render, redirect
from .models import Msg

def index(request):

    if request.method == 'POST':
        data = Msg(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        data.save()
        return redirect('home.html')
    return render(request, 'home.html')