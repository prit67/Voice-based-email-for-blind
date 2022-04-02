from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^',include('homepage.urls')),
    
]
