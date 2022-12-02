
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render, HttpResponse
from . import views
# Create your views here.


# def home(request):
#     return HttpResponse('<h2 style="color:red">DRL HOME PAGE</h2>')


urlpatterns = [
    path('main/', views.main, name='main'),
    path('admin/', admin.site.urls, name='admin'),

    path('predict/', views.predict, name='predict'),
    path('info/', views.info, name='info'),
    path('projects/', include('projects.urls')),
    # path('users', include('users.urls')),
    # path('runs/', include('runs.urls')),
    # path('classroom/', include('classroom.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
