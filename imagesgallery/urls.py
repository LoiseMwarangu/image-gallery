
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^recent/$',views.photo_date,name='photosToday'), 
    url(r'^search/', views.search, name='search_results'),
    url(r'^image/(\d+)',views.posted_photos,name='posted_photos')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


