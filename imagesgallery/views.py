from django.http  import HttpResponse,Http404

import datetime as dt

from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photo_date(request):
    date = dt.date.today()
    return render(request, 'all-photos/recent.html', {"date": date,})

def posted_photos(request):
    images = Image.all_images()
    return render(request, 'all-photos/index.html' , {"images":images})
  
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

def photo(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"index.html",{"image":image})