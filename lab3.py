from PIL import Image, ImageChops
import os
import math
from lab2 import Bradley_Rot

def difference_images(img1, img2):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    result = ImageChops.difference(img1.convert('1'), img2.convert('1'))
    inv_img = ImageChops.invert(result)
    inv_img.save(SOURE_DIR+"\\res_inter8.png")
    return inv_img

def sum_pix(integral_img, x, y, a, b):
    sum = (0,0,0)
    indent = 1
    if y+indent>=b or x + indent >= a:
        ##print("First if")
        if y+indent>=b and x + indent >= a:
            ##print("First if 1")
            x = a - 1
            y = b - 1
            k = integral_img[x][y][0] - integral_img[x-indent-1][y][0] - integral_img[x][y-indent-1][0] + integral_img[x-indent-1][y-indent-1][0]
            m = integral_img[x][y][1] - integral_img[x-indent-1][y][1] - integral_img[x][y-indent-1][1] + integral_img[x-indent-1][y-indent-1][1]
            n = integral_img[x][y][2] - integral_img[x-indent-1][y][2] - integral_img[x][y-indent-1][2] + integral_img[x-indent-1][y-indent-1][2]
            sum = (k,m,n)
        elif y <=indent <= x and x + indent >= a:
            ##print("First if 2")
            k = integral_img[a-1][y+indent][0]-integral_img[x-indent-1][y+indent][0]
            m = integral_img[a-1][y+indent][1]-integral_img[x-indent-1][y+indent][1]
            n = integral_img[a-1][y+indent][2]-integral_img[x-indent-1][y+indent][2]
            sum = (k,m,n)
        elif x <=indent <= y and y + indent >= b:
            ##print("First if 3")
            k = integral_img[x+indent][b-1][0]-integral_img[x+indent][y-indent-1][0]
            m = integral_img[x+indent][b-1][1]-integral_img[x+indent][y-indent-1][1]
            n = integral_img[x+indent][b-1][2]-integral_img[x+indent][y-indent-1][2]
            sum = (k,m,n)
        elif y + indent >= b:
            ##print("First if 4")
            k = integral_img[x+indent][b-1][0]-integral_img[x+indent][y-indent-1][0]-integral_img[x-indent-1][b-1][0]+integral_img[x-indent-1][y-indent-1][0]
            m = integral_img[x+indent][b-1][1]-integral_img[x+indent][y-indent-1][1]-integral_img[x-indent-1][b-1][1]+integral_img[x-indent-1][y-indent-1][1]
            n = integral_img[x+indent][b-1][2]-integral_img[x+indent][y-indent-1][2]-integral_img[x-indent-1][b-1][2]+integral_img[x-indent-1][y-indent-1][2]
            sum = (k,m,n)
        elif x+indent >= a:
            ##print("First if 5")
            k = integral_img[a-1][y+indent][0]-integral_img[a-1][y-indent-1][0]-integral_img[x-indent-1][y+indent][0]+integral_img[x-indent-1][y-indent-1][0]
            m = integral_img[a-1][y+indent][1]-integral_img[a-1][y-indent-1][1]-integral_img[x-indent-1][y+indent][1]+integral_img[x-indent-1][y-indent-1][1]
            n = integral_img[a-1][y+indent][2]-integral_img[a-1][y-indent-1][2]-integral_img[x-indent-1][y+indent][2]+integral_img[x-indent-1][y-indent-1][2]
            sum = (k,m,n)
        return sum
    if x > indent and y > indent:
        ##print("Second if 1")
        ##print(a," ",x," ",b," ",y," ",indent)
        k = integral_img[x+indent][y+indent][0]-integral_img[x-indent-1][y+indent][0]-integral_img[x+indent][y-indent-1][0]+integral_img[x-indent-1][y-indent-1][0]
        m = integral_img[x+indent][y+indent][1]-integral_img[x-indent-1][y+indent][1]-integral_img[x+indent][y-indent-1][1]+integral_img[x-indent-1][y-indent-1][1]
        n = integral_img[x+indent][y+indent][2]-integral_img[x-indent-1][y+indent][2]-integral_img[x+indent][y-indent-1][2]+integral_img[x-indent-1][y-indent-1][2]
        sum = (k,m,n)
    elif y<=indent<=x:
        ##print("Second if 2")
        k = integral_img[x-indent-1][y+indent][0]
        m = integral_img[x-indent-1][y+indent][1]
        n = integral_img[x-indent-1][y+indent][2]
        sum = (-k,-m,-n)
    elif x<=indent<=y:
        ##print("Second if 3")
        k = integral_img[x+indent][y-indent-1][0]
        m = integral_img[x+indent][y-indent-1][1]
        n = integral_img[x+indent][y-indent-1][2]
        sum = (-k,-m,-n)
    elif x<indent and y<indent:
        ##print("Second if 4")
        k = integral_img[x][y][0]
        m = integral_img[x][y][1]
        n = integral_img[x][y][2]
        sum = (k,m,n)
    return sum

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

def dilation(img):
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    print("Операция - морфологическое расширение Dilation")
    a = int(img.size[0])
    b = int(img.size[1])
    ##Интегральное изображение - массив пикселей вида (_,_,_)
    integral_img = integral(img)
    res_image = Image.new("1", (a, b))
    for x in range(a):
        for y in range(b):
            pix = img.getpixel((x, y))
            m = sum_pix(integral_img, x, y, a, b)[0] - pix[0]
            n = sum_pix(integral_img, x, y, a, b)[1] - pix[1]
            k = sum_pix(integral_img, x, y, a, b)[2] - pix[2]
            if m+n+k > 0:
                res_image.putpixel((x,y),255)
            else:
                res_image.putpixel((x,y),0)
    res_image.save(SOURE_DIR+"\\res_inter7.png")
    return res_image


def lab3():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\images\\'
    content = os.listdir(SOURE_DIR)
    print(content)
    name = input()
    img = Image.open(SOURE_DIR+name+".png")
    a = int(img.size[0])
    b = int(img.size[1])
    print("Размер png на входе:",a,b)
    img = Bradley_Rot(img,0.005)
    res1 = dilation(img)
    difference_images(img,res1)