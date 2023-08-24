from django.contrib import admin
from django.urls import path, include
from home.views import *
urlpatterns = [
    path('', home, name='home'),
    # path('', portfolio, name='portfolio'),
    path('portfolio/', portfolio, name='portfolio'),
    path('jira/', jira, name='jira'),
    path('contact-us/', contact_us, name='contact_us'),
   
    
]