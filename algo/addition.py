import os
from re import L
import sys

import numpy as np
from numpy import asarray
import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

np.set_printoptions(threshold=sys.maxsize)


def addition_decode_algo(stego_path):
    stego_image = Image.open(stego_path, 'r')
    stego_array = np.array(list(stego_image.getdata()))

    if stego_image.mode == 'RGB':
        n = 3
        # steg_image = PIL.Image.new(mode="RGB", size=(200, 200))
    elif stego_image.mode == 'RGBA':
        n = 4
        # steg_image = PIL.Image.new(mode="RGBA", size=(200, 200))

    total_pixels_steg = stego_array.size//n
    width_stego, height_stego = width_c, height_c = stego_image.size
    # print(stego_array.size)
    # print(width_c," ",height_c)
    total_pixels_c = width_c*height_c
    total_pixels_s = total_pixels_steg - total_pixels_c

    rows_s, cols_s = (total_pixels_s, n)
    rows_c, cols_c = (total_pixels_c, n)
    container_array = [[0]*cols_c]*rows_c
    sink_array = [[0]*cols_s]*rows_s

    for p in range(total_pixels_steg):
        for q in range(n):
            container_array[p][q] = stego_array[p][q]

    for p in range(total_pixels_steg, len(stego_array)):
        for q in range(0, n):
            sink_array[p-total_pixels_steg][q] = stego_array[p][q]

    # container_array=np.arange(0,total_pixels_c, 1,np.uint8)
    # container_array=np.reshape(container_array,(1080,1920))
    # container_image=Image.fromarray(container_array)
    # container_image.save(stego_path+"Container.jpg")

    # container_image = Image.fromarray(np.array(container_array).astype(np.uint8))
    # container_image= np.array(container_array).astype(np.uint8)

    # sink_image = Image.fromarray(np.array(sink_array).astype(np.uint8))
    # sink_image = np.array(sink_array).astype(np.uint8)

    # saving the final output
    # as a PNG file

    # container_image = container_image.save(stego_path+"ContainerImage.png")
    # sink_image = sink_image.save(stego_path+"SinkImage.png")

    container_image = Image.fromarray(
        container_array.astype('uint8'), stego_image.mode)
    sink_image = Image.fromarray(sink_array.astype('uint8'), stego_image.mode)

    return ""


def addition_encode_algo(container_path, sink_path):
    container_image = Image.open(container_path, 'r')
    sink_image = Image.open(sink_path, 'r')
    # steg_image = Image.open(container_path, 'r')

    destination_path = "Stego_.jpeg"

    # steg_image = steg_image.save(destination_pat

    # destination_path = os.path.splitext(container_path)[0]+"Encrypted.png"

    width_c, height_c = container_image.size
    print(width_c, " ", height_c)
    width_s, height_s = sink_image.size

    if(width_s > width_c or height_s > width_c):
        print('Error! Sink image too big!')
        return container_path
    # container_array = asarray(container_image)
    # sink_array=asarray(sink_image)
    # steg_array=asarray(steg_image)
    container_array = np.array(list(container_image.getdata()))
    sink_array = np.array(list(sink_image.getdata()))
    steg_array = container_array.copy()
    temp_array = container_array.copy()

    data_c = []  # r,g,b,i,j
    k = 0
    for i in range(height_c):
        temp = []
        for j in range(width_c):
            temp.append(container_array[k])
            k += 1
        data_c.append(temp)

    data_s = []  # r,g,b,i,j
    k = 0
    for i in range(height_s):
        temp = []
        for j in range(width_s):
            temp.append(sink_array[k])
            k += 1
        data_s.append(temp)

    steg_array = data_c.copy()

    n = 5

    # newsize = (width_c*n, height_c*n)
    # steg_array = steg_array.resize(newsize)

    image_resized = []
    for i in range(height_c):
        temp = []
        for j in range(width_c):
            for k in range(n):
                temp.append(data_c[i][j][0:3])
        for k in range(n):
            image_resized.append(temp)

    print(len(image_resized[0]))
    for i in range(len(data_s)):
        for j in range(len(data_s[0])):
            p = int((i+1)*(n-1))
            q = int((j+1)*(n-1))
            image_resized[p][q] = data_s[i][j][0:3]

    # img_res = []
    # for i in range(len(image_resized)):
    #     for j in range(len(image_resized[0])):
    #         img_res.append(image_resized[i][j])

    img_res = np.array(image_resized)

    steg_image = Image.fromarray(
        img_res, "RGB")

    # print(steg_image.size)
    steg_image = steg_image.save(destination_path)
    # print("Image Encoded Successfully")
    # print(width_c, " ", height_c)

    return destination_path
