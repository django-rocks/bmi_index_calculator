from django.shortcuts import render

def example_view(request):
    return (request, 'core/example.html')
