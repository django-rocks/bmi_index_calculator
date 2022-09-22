from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    my_var = {'height':1.87,'weight':120}
    return render(request, 'core/example.html',context=my_var)
# def index(request):
#    return HttpResponse("Howzit")
def feedback_review(request):
    return render(request, 'core/feedback.html')
