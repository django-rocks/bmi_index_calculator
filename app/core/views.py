from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    return render(request, 'core/example.html')
# def index(request):
#    return HttpResponse("Howzit")
