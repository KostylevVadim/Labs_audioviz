from PIL import Image, ImageChops
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lab2.lab2 import Bradley_Rot
def get_prof(img):
    print("Getting profiles")
    width = img.size[0]
    height= img.size[1]
    x_prof = []
    y_prof = []
    for x in range(width):
        br=0
        for y in range(height):
            
            if img.getpixel((x,y))[0] == 0 and img.getpixel((x,y))[1] == 0 and img.getpixel((x,y))[2] == 0:
                br = br+1
        
        x_prof.append(br)
    for y in range(height):
        br=0
        for x in range(width):
            if img.getpixel((x,y))[0] == 0 and img.getpixel((x,y))[1] == 0 and img.getpixel((x,y))[2] == 0:
                br = br+1
        y_prof.append(br)
    
    return x_prof, y_prof


def reference_image(img):
    pix = img.load()
    width, height = img.size[0], img.size[1]
    hor_p = [0 for _ in range(width)]
    ver_p = [0 for _ in range(height)]
    for i in range(width):
        for j in range(height):
            pixel = img.getpixel((i,j))
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                hor_p[i] += 1
                ver_p[j] += 1
    x0, y0, x1, y1 = 0, 0, width, height
    #print(hor_p, ver_p)
    for i in range(width):
        if hor_p[i] > 0:
            x0 = i
            break
    for i in range(width - 1, -1, -1):
        if hor_p[i] <= 0:
            x1 = i
        else:
            break

    for i in range(height):
        if ver_p[i] > 0:
            y0 = i
            break

    for i in range(height - 1, -1, -1):
        if ver_p[i] <= 0:
            y1 = i
        else:
            break
    #print(x0, y0, x1, y1)
    new_sz = (x0, y0, x1, y1)
    return img.crop(new_sz)


def hists(res):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new/'
    SOURE_DIR1 = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\hists/'
    for i in range(len(res)):
        img = Image.open(SOURE_DIR+ str(i) + ".bmp")
        #img = reference_image(img)
        x_profile, y_profile = get_prof(img)
        fig, axs = plt.subplots(1, 2, figsize=(9, 3))

        axs[0].bar(np.arange(0, len(x_profile)), height=x_profile)
        axs[1].barh(np.arange(0, len(y_profile)), width=y_profile)

        plt.savefig(SOURE_DIR1+str(i)+".png", dpi=70)
        del fig
        del axs

def Segmentization(img):
    #print("Начинаем сегмантизацию")
    #s="𐎀𐎁𐎂𐎃𐎄𐎅𐎆𐎇𐎈𐎉𐎊𐎋𐎌𐎍𐎎𐎏𐎐𐎑𐎒𐎓𐎔𐎕𐎖𐎗𐎘𐎙𐎚𐎛𐎜𐎝"
    x_prof, y_prof = get_prof(img)
    ep = 0
    res = []
    #print(x_prof)
    for i in range(len(x_prof)-3):
        #print('here1')
        #step = 0
        if x_prof[i] <= ep and x_prof[i+2] <= ep and x_prof[i+3] <= ep:
            #print('here2', x_prof[i])
            step = 0
        else:
            #print('here3')
            step += 1
            right = i
            left = right - step
            if x_prof[i+1] <= ep and x_prof[i+2] <= ep and x_prof[i+3] <= ep and x_prof[i+4] <= ep and x_prof[i+5] <= ep :
                #print('here4')
                res.append((left, right))
    #print(res)
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new/'
    #print(img.size[0],img.size[1])
    for i in range(len(res)):
        left, right = res[i]
        
        #print(left, 0,right)
        new_img = img.crop((left, 0, right+1, img.size[1]-1))
        #print(new_img.size)
        new_img = reference_image(new_img)
        #print(new_im.size)
        new_img.save(SOURE_DIR+ str(i) + ".bmp", mode="1")
    hists(res)
    return res

def lab6():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\images\\'
    content = os.listdir(SOURE_DIR)
    #print(content)
    ##name = input()
    img = Image.open(SOURE_DIR+"string.bmp")
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    img = Bradley_Rot(img,0.1)
    Segmentization(img)