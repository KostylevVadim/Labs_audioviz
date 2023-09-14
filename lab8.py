from PIL import Image, ImageChops
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def semitone(img):

    if str(img.mode) == "L":
        return img

    width = img.size[0]
    height = img.size[1]

    new_image = Image.new("L", (width, height))

    for x in range(width):
        for y in range(height):
            pix = img.getpixel((x, y))

            sum = sum(pix) // 3
            new_image.putpixel((x, y), int(sum))
            
    return new_image


def get_haralic(img):
    print('Getting Haralic')
    
    img_matrix = np.asarray(img).transpose()

    width = img.size[0]
    height = img.size[1]
    har_size = 256
    matrix = np.zeros((har_size, har_size))

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pix = img_matrix[x, y]

            up_pix = img_matrix[x+1, y - 1]
            down_pix = img_matrix[x+1, y + 1]
            left_pix = img_matrix[x - 1, y+1]
            right_pix = img_matrix[x + 1, y-1]

            matrix[pix, up_pix] += 1
            matrix[pix, down_pix] += 1
            matrix[pix, left_pix] += 1
            matrix[pix, right_pix] += 1

    max_ = np.max(matrix)

    if max_ > 256:
        matrix = (matrix * 256) // max_

    return Image.fromarray(matrix).convert("L"), matrix


def attribute(matrix, img):
    print('Getting Attribute')
    m = 0
    #m2 = 0
    #m1 = m2
    oi2, oj2 = 0, 0
    width = img.size[0]
    height = img.size[1]
    #matrix = np.zeros((l, l))
    PI = []
    for i in range(256):
        s1 = 0
        for j in range(256):
            s1+= matrix[i,j]
        m+= i*s1
    
    for i in range(256):
        s1 = 0
        for j in range(256):
            s1+= matrix[i,j]
        oj2+=(i - m) * (i - m) * s1
    
    for j in range(256):
        s1 = 0
        for i in range(256):
            #print(matrix[i,j])
            s1+= matrix[i,j]
        #print((j - m) * (j - m) * s1, s1)
        oi2+=(j - m) * (j - m) * s1
    CORR = 0
    for i in range(256):
        for j in range(256):
            CORR+= i*j*matrix[i,j] - m*m
    
    CORR = CORR/(math.sqrt(oi2*oj2))
    return CORR

def get_hist(matrix, nm):
    sh = np.reshape(matrix, (1, -1))

    plt.figure(nm)
    plt.hist(sh[0], bins=256)

    plt.savefig(f"hists8/{nm}.png")

def normalize(matrix):
    max_image = np.max(matrix)
    return matrix / max_image, max_image

def get_semitone_asarray(matrix):
    return np.sum(matrix, axis=1) // 3

def contrast(matrix, c, f, y, name):
    norm_matrix, max_image = normalize(matrix)

    norm_new_matrix = c * (norm_matrix + f / max_image) ** y
    norm_new_matrix[norm_new_matrix > 1] = 1
    new_matrix = (norm_new_matrix * max_image).astype("uint8")

    img = Image.fromarray(new_matrix, mode="L").save(
        f"results/{name}.png"
    )
    return new_matrix, img


def lab8():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\images\\'
    content = os.listdir(SOURE_DIR)
    print(content)
    name = input()
    img = Image.open(SOURE_DIR+name+".png")
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    img_n = semitone(img)
    img_res, matrix_res = get_haralic(img_n)
    img_res.save(f"{name+'semi'}_har.png")
    print(attribute(matrix_res, img_n))
    matrix = np.asarray(img_n)
    matrix_new, img = contrast(matrix, float(1), float(0.1), float(0.1), name)
    get_hist(matrix, name)
    get_hist(matrix_new, name+'_after_contrast')
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\results\\'
    img = Image.open(SOURE_DIR+name+".png")
    img_res, matrix_res = get_haralic(img)
    img_res.save(f"{name+'cont'}_har.png")
 