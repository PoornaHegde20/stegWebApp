from django.urls import reverse
from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse

from numpy import imag

# from sympy import re
from .models import LSBEncode, LSBDecode
from .forms import ImageFormEncode, ImageFormDecode
from algo.lsb import lsb_encode_algo, lsb_decode_algo
from django.template.response import TemplateResponse


def index(request):
    return render(request, 'steg/index.html')


def lsb_encode(request):

    form = ImageFormEncode(request.POST or None, request.FILES or None)
    if form.is_valid():
        lsb_encode_model = form.save(commit=True)
        image_path = lsb_encode_model.inputImagePath
        image_id = lsb_encode_model.id
        # lsb_encode_model.algorithm = form.cleaned_data['algorithm']
        lsb_encode_model.message = form.cleaned_data['message']
        image_path = "media/"+str(image_path)
        # if lsb_encode_model.algorithm == 'LSB':
        output_path = lsb_encode_algo(str(image_path), lsb_encode_model.message)
        lsb_encode_model.outputImagePath = output_path[6:]
        lsb_encode_model.save()
        return redirect(lsb_encode_model)

    context = {
        'form': form
    }

    return render(request, 'steg/lsbEncoder.html', context)


def index_decode(request):

    form = ImageFormDecode(request.POST or None, request.FILES or None)
    if form.is_valid():
        lsb_decode_model = form.save(commit=True)
        image_path = lsb_decode_model.inputImagePath
        image_id = lsb_decode_model.id
        # lsb_decode_model.algorithm = form.cleaned_data['algorithm']
        image_path = "media/"+str(image_path)
        # print(image_id, image_path)
        # if lsb_decode_model.algorithm == 'LSB':
        message = lsb_decode_algo(str(image_path))

        # else:
        #     message = mnf_decode_algo(
        #         str(image_path))
        # args={}
        # args['key'] = message
        lsb_decode_model.message=message
        lsb_decode_model.save()
        image_path = lsb_decode_model.inputImagePath
        image_id = lsb_decode_model.id
        return redirect(lsb_decode_model)

    context = {
        'form': form
    }

    return render(request, 'steg/decode.html',context)


def show_image(request, id):
    image = LSBEncode.objects.filter(id=id).first()
    if image:
        return render(request, 'steg/show_image.html', {
            'image': image
        })
    pass


def show_image_decode(request, id):
    image = LSBDecode.objects.filter(id=id).first()
    if image:
        return render(request, 'steg/show_image_decode.html', {
            'image': image
        })
    pass

def decode(request):
    return render(request, 'steg/decode.html')


def encode(request):
    return render(request, 'steg/encode.html')

def addition_encode(request):
    return render(request, 'steg/additionEncoder.html')

# def lsbEncode(request):
#     return render(request, 'steg/lsbEncode.html')


# def lsbDecode(request):
#     return render(request, 'steg/decode.html')
