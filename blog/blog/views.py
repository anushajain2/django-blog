from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #render the request using the template provided
    return render(request, 'home.html')


def about(request):
    #request is the object received from the browser
    return render(request, 'about.html')