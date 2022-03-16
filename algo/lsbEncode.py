# import all the required libraries

import cv2 as cv
import numpy as np
import types

def textToBinary(text):
    if type(text) == str:
        return ''.join([format(ord(i), "08b") for i in text])
    elif type(text) == bytes or type(text) == np.ndarray:
        return [format(i, "08b") for i in text]
    elif type(text) == int or type(text) == np.uint8:
        return format(text, "08b")
    else:
        raise TypeError("Input type not supported")


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def encryptData(image, message):

    # calculate the maximum bytes to encode
    total_bytes = image.shape[0] * image.shape[1] * 3 // 8

    # Check if the number of bytes to encode is less than the maximum bytes in the image
    if len(message) > total_bytes:
        raise ValueError(
            "Error! Data too big and picture too small!")

    message += "#####"  # delimeter

    message_index = 0

    message_in_binary = textToBinary(message)

    data_length = len(message_in_binary)
    for values in image:
        for pixel in values:
            # convert RGB values to binary format
            r, g, b = textToBinary(pixel)
            if message_index < data_length:
            # hide the data into least significant bit of red,green and blue pixel
                temp = int(message_in_binary[message_index])
                if temp == 1:
                    pixel[0] = int(int(decimalToBinary(pixel[0])) | 1)
                else:
                    pixel[0] = int(0 & int(decimalToBinary(pixel[0])))
                message_index += 1
            if message_index < data_length:
                temp = int(message_in_binary[message_index])
                if temp == 1:
                    pixel[1] = int(int(decimalToBinary(pixel[1])) | 1)
                else:
                    pixel[1] = int(int(decimalToBinary(pixel[1])) & 0)
                message_index += 1
            if message_index < data_length:
                temp = int(message_in_binary[message_index])
                if temp == 1:
                    pixel[2] = int(int(decimalToBinary(pixel[2])) | 1)
                else:
                    pixel[2] = int(int(decimalToBinary(pixel[2])) & 0)
                message_index += 1
            # if data is encoded, just break out of the loop
            if message_index >= data_length:
                break

    return image

def encode_text(image_name):
    # image_name = input("Enter image name(with extension): ")
    image = cv.imread(image_name) 
    # resized_image = cv.resize(image, (500, 500))

    data = input("Enter data to be encoded : ")
    if (len(data) == 0):
        raise ValueError('Data is empty')

    filename = input("Enter the name of new encoded image(with extension): ")
    encoded_image = encryptData(image, data)
    cv.imwrite(filename, encoded_image)


encode_text('bg.jpg')
