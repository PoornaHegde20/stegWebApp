from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import lsbEncoding
from .forms import ImageForm


def showImage(request):

    lastimage = lsbEncoding.objects.last()

    inputImagePath = lastimage.inputImagePath

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'inputImagePath': inputImagePath,
               'form': form
               }

    return render(request, 'steg/upload.html', context)


def index(request):
    return render(request, 'steg/index.html')

def decode(request):
    return render(request,'steg/decode.html')


def encode(request):
    return render(request, 'steg/encode.html')


def lsbEncode(request):
    return render(request, 'steg/lsbEncode.html')


def lsbDecode(request):
    return render(request, 'steg/lsbDecode.html')
