# import all the required libraries

import cv2
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


def decryptData(image):
    message_in_binary = ""
    for values in image:
        for pixel in values:
            # convert the red,green and blue values into binary format
            r, g, b = textToBinary(pixel)
            # extracting data from the least significant bit of red pixel
            message_in_binary += r[-1]
            # extracting data from the least significant bit of red pixel
            message_in_binary += g[-1]
            # extracting data from the least significant bit of red pixel
            message_in_binary += b[-1]

    # split by 8-bits
    message_in_bytes = [message_in_binary[i: i+8]
                        for i in range(0, len(message_in_binary), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in message_in_bytes:
        decoded_data += chr(int(byte, 2))
        # check if we have reached the delimeter which is "#####"
        if decoded_data[-5:] == "#####":
            break
    # remove the delimeter to show the original hidden text
    return decoded_data[:-5]


# Decode the data in the image
def decode_text(image_name):
    # image_name = input(
    #     "Enter the name of the steganographed image that you want to decode (with extension) :")
    image = cv2.imread(image_name) 

    print("The Steganographed image is as shown below: ")
    # resized_image = cv2.resize(image, (500, 500))
    # cv2.imshow("Resized image",resized_image) #display the Steganographed image

    text = decryptData(image)
    return text

# decode_text('bg1.jpg')
