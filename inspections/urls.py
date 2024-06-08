from django.urls import path
from .views import upload_file, live_search


urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('search/', live_search, name='search'),
]
