from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return (request, 'core/example.html')
# def index(request):
#    return HttpResponse("Howzit")
