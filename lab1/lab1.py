from PIL import Image, ImageChops
import os
import math

def inter(img, m):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    a1 = int(a*m-1)
    b1 = int(b*m-1)
    res_image = Image.new("RGB", (a1,b1))
    for i in range(a1):
        for j in range(b1):
            pixel = img.getpixel((i/m,j/m))
            res_image.putpixel((i,j),pixel)
    
    res_image.save(SOURE_DIR+"\\res_inter.png")
    a = int(res_image.size[0])
    b = int(res_image.size[1])
    print("Размер png на выходе:",a,b)

def decim(img, m):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    a1 = int(a/m-1)
    b1 = int(b/m-1)
    res_image = Image.new("RGB", (a1,b1))
    for i in range(a1):
        for j in range(b1):
            pixel = img.getpixel((i*m,j*m))
            res_image.putpixel((i,j),pixel)
    res_image.save(SOURE_DIR+"\\res_inter1.png")
    a = int(res_image.size[0])
    b = int(res_image.size[1])
    print("Размер png на выходе:",a,b)

def interdecim(img, m, n):
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    a1 = int(a*m-1)
    b1 = int(b*m-1)
    res_image = Image.new("RGB", (a1,b1))
    for i in range(a1):
        for j in range(b1):
            pixel = img.getpixel((i/m,j/m))
            res_image.putpixel((i,j),pixel)
    decim_for_interdecim(res_image, n)

def decim_for_interdecim(img, m):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    a = int(img.size[0])
    b = int(img.size[1])
    a1 = int(a/m-1)
    b1 = int(b/m-1)
    res_image = Image.new("RGB", (a1,b1))
    for i in range(a1):
        for j in range(b1):
            pixel = img.getpixel((i*m,j*m))
            res_image.putpixel((i,j),pixel)
    res_image.save(SOURE_DIR+"\\res_inter3.png")
    a = int(res_image.size[0])
    b = int(res_image.size[1])
    print("Размер png на выходе:",a,b)

def rediscritization(img, m):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    a1 = int(a*m-1)
    b1 = int(b*m-1)
    res_image = Image.new("RGB", (a1,b1))
    for i in range(a1):
        for j in range(b1):
            pixel = img.getpixel((i/m,j/m))
            res_image.putpixel((i,j),pixel)
    
    res_image.save(SOURE_DIR+"\\res_inter4.png")
    a = int(res_image.size[0])
    b = int(res_image.size[1])
    print("Размер png на выходе:",a,b)


def lab12():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\images\\'
    content = os.listdir(SOURE_DIR)
    print(content)
    name = input()
    img = Image.open(SOURE_DIR+name+".png")
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    print("1 - inter 2 - decim 3 - interdecim 4 - rediscritization")
    ch = int(input())
    if(ch==1):
        print("Во сколько раз увеличить")
        m = int(input())
        inter(img, m)
    if(ch==2):
        print("Во сколько раз уменьшить")
        m = int(input())
        decim(img, m)
    if(ch==3):
        print("Во сколько раз увеличить")
        m = int(input())
        print("Во сколько раз уменьшить")
        n = int(input())
        interdecim(img, m, n)
    if(ch==4):
        print("Во сколько раз увеличить")
        m = int(input())
        print("Во сколько раз уменьшить")
        n = int(input())
        k = float(m/n)
        rediscritization(img, k)