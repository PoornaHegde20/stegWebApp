
from . import views
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.showImage, name='upload')
    path('/decode', views.decode, name='decode'),
    path('/encode', views.encode, name='encode'),
    path('/lsbDecode', views.lsbDecode, name='lsbDecode'),
    path('/lsbEncode', views.lsbEncode, name='lsbEncode'),

]
