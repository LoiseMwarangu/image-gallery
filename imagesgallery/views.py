from django.http  import HttpResponse,Http404

import datetime as dt
from .models import *
from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def posted_photos(request):
    images = Image.all_images()
    return render(request, 'index.html' , {"images":images})
  
def search(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})
    else:
        message = "hate to break it to you but this category has no photos yet "
        return render(request, 'search.html',{"message":message})
    return render(request,"search.html")    

