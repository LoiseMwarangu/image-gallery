
from django.http  import HttpResponse,Http404

import datetime as dt

from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photo_date(request):
    date = dt.date.today()
    return render(request, 'all-photos/recent.html', {"date": date,})

