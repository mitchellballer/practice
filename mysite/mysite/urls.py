"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
include() allows referencing other URLconfs. 
Django will 'chop off' whatever part of the part of the URL matched up to that point
Sends the remaining string to the included URLconf for further processing
So urls in polls/urls.py ex /polls/, /fun_polls/, /content/polls/ etc will work

Path argument: path(route, view, kwargs, name)
route: required, string containing url pattern. 
    Start at first pattern in  urlpatterns and goes through until it finds a match
view: required, function to be called with HttpRequest as first argument and any kwargs
kwargs: optional, arguments to be passed in a dictionary to target view
name: optional, allows you to refer to rul unambiguously from elsewhere.
    Can make global changes to URL patterns from a single file
"""
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
