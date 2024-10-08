from django.shortcuts import render

# Create your views here.

def indexView(requets, *args, **kwargs):
    
    return render(requets, 'home-2.html', {})