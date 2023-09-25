from PIL import Image, ImageChops
import os
import math

def semi(img):
    print('Doing semitone')
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    res_image = Image.new("RGB", (a,b))
    for x in range(a):
        for y in range(b):
            pix = img.getpixel((x, y))
            sum = 0.3 * pix[0] + 0.59 * pix[1] + 0.11 * pix[2]
            res_image.putpixel((x, y), (int(sum), int(sum), int(sum)))
    res_image.save(SOURE_DIR+"\\res_inter5.png")
    return res_image

def integral(img):
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    res_img = [[(0,0,0) for j in range(b)] for i in range(a)]
    
    for x in range(a):
        ##print(x)
        for y in range(b):
            pix = img.getpixel((x,y))
            new_pix = (0,0,0)
            if x == 0 and y == 0:
                new_pix = (pix[0], pix[1], pix[2])
            elif x == 0 and y > 0:
                new_pix = (pix[0] + res_img[x][y-1][0], pix[1] + res_img[x][y-1][1], pix[2] + res_img[x][y-1][2])
                #new_pix = pix + res_img.getpixel((x,y-1))
            elif x > 0 and y == 0:
                new_pix = (pix[0] + res_img[x-1][y][0], pix[1] + res_img[x-1][y][1], pix[2] + res_img[x-1][y][2])
            else:
                m = pix[0] + res_img[x-1][y][0] + res_img[x][y-1][0] - res_img[x-1][y-1][0]
                n = pix[1] + res_img[x-1][y][1] + res_img[x][y-1][1] - res_img[x-1][y-1][1]
                k = pix[2] + res_img[x-1][y][2] + res_img[x][y-1][2] - res_img[x-1][y-1][2]
                new_pix = (m,n,k)
            
            res_img[x][y] = new_pix
            ##print(x, res_img[x][y])
    return res_img

def Bradley_Rot(img,t):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    a = int(img.size[0])
    b = int(img.size[1])
    ##print("Размер png на входе:",a,b)
    res_image = Image.new("RGB", (a,b))
    S = b//8
    s = S//2
    ##t = 0.05
    integral_img = integral(img)
    for x in range(a):
        for y in range(b):
            x1 = x-s
            x2 = x+s
            y1 = y-s
            y2 = y+s
            if(x1<0):
                x1 = 0
            if(x2>=x):
                x2 = a-1
            if(y1<0):
                y1=0
            if(y2>=y):
                y2=b-1
            count = (x2-x1)*(y2-y1)
            m = integral_img[x1][y1][0] - integral_img[x2][y1][0] - integral_img[x1][y2][0] + integral_img[x2][y2][0]
            n = integral_img[x1][y1][1] - integral_img[x2][y1][1] - integral_img[x1][y2][1] + integral_img[x2][y2][1]
            k = integral_img[x1][y1][2] - integral_img[x2][y1][2] - integral_img[x1][y2][2] + integral_img[x2][y2][2]
            pixel = img.getpixel((x,y))
            pixel2 = (m*(1-t),n*(1-t),k*(1-t))
            l = img.getpixel((x,y))[0] * count
            o = img.getpixel((x,y))[1] * count
            p = img.getpixel((x,y))[2] * count
            if((l<pixel2[0]) and (o<pixel2[1]) and(p<pixel2[2])):
                res_image.putpixel((x,y),(0,0,0))
            else:
                res_image.putpixel((x,y),(255,255,255))
    res_image.save(SOURE_DIR+"\\res_inter6.png")
    return res_image

def lab2():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\images\\'
    content = os.listdir(SOURE_DIR)
    print(content)
    name = input()
    img = Image.open(SOURE_DIR+name+".png")
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    print("1 - semi 2 - bin")
    ch = int(input())
    if(ch==1):
        semi(img)
    if(ch==2):
        print("Введите t:")
        t = float(input())
        Bradley_Rot(img,t)
