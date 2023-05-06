from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def BASE(request):
    return render(request, 'base.html')
