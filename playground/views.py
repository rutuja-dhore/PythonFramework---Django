from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler

def say_hello(request):
    x1 = 1
    x2 = 2

    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name' : 'Rutuja Dhore'} )