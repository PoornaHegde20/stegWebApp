from django.urls import reverse
from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse

from numpy import imag
from .models import LSBEncode
from .forms import ImageFormEncode, ImageFormDecode
from algo.lsb import lsb_encode_algo, lsb_decode_algo
from django.template.response import TemplateResponse


def index(request):
    return render(request, 'steg/index.html')


def index_encode(request):

    form = ImageFormEncode(request.POST or None, request.FILES or None)
    if form.is_valid():
        lsb_model = form.save(commit=False)
        image_path = lsb_model.inputImagePath
        image_id = lsb_model.id
        lsb_model.algorithm = form.cleaned_data['algorithm']
        lsb_model.message = form.cleaned_data['message']
        image_path = "media/"+str(image_path)
        if lsb_model.algorithm == 'LSB':
            output_path = lsb_encode_algo(str(image_path), lsb_model.message)
        lsb_model.outputImagePath = output_path[6:]
        lsb_model.save()
        return redirect(lsb_model)

    context = {
        'form': form
    }

    return render(request, 'steg/encode.html', context)


def index_decode(request):

    form = ImageFormDecode(request.POST or None, request.FILES or None)
    if form.is_valid():
        lsb_decode_model = form.save(commit=False)
        image_path = lsb_decode_model.inputImagePath
        image_id = lsb_decode_model.id
        lsb_decode_model.algorithm = form.cleaned_data['algorithm']
        image_path = "media/images/"+str(image_path)
        # print(image_id, image_path)
        if lsb_decode_model.algorithm == 'LSB':
            message = lsb_decode_algo(str(image_path))

        # else:
        #     message = mnf_decode_algo(
        #         str(image_path))
        # args={}
        # args['key'] = message
        lsb_decode_model.save()
        image_path = lsb_decode_model.inputImagePath
        image_id = lsb_decode_model.id
        # print(image_id, image_path)
        return render('steg/decode-show.html')
    context = {
        'form': form
    }

    return TemplateResponse(request, 'steg/decode.html', args)


def show_image(request, id):
    image = LSBEncode.objects.filter(id=id).first()
    if image:
        return render(request, 'steg/show_image.html', {
            'image': image
        })
    pass

# def decode(request):
#     return render(request, 'steg/decode.html')


# def encode(request):
#     return render(request, 'steg/encode.html')


def lsbEncode(request):
    return render(request, 'steg/lsbEncode.html')


def lsbDecode(request):
    return render(request, 'steg/lsbDecode.html')
