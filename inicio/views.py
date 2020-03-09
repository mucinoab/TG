from django.shortcuts import render

# Create your views here.
def inicio_views (request):
    return render (request,'base.html')
