
from . import views
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'steg'
urlpatterns = [
    # path('upload', views.index_encode, name='upload'),
    path('', views.index, name='index'),

    path('show-image/<int:id>/', views.show_image, name='show_img'),
    path('decode', views.index_decode, name='decode'),
    path('encode', views.index_encode, name='encode'),
    path('lsbDecode', views.lsbDecode, name='lsbDecode'),
    path('lsbEncode', views.lsbEncode, name='lsbEncode'),

]
