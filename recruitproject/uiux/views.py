from django.shortcuts import render

# Create your views here.
def uiux(request): 
    return render(request, 'index.html', {})  