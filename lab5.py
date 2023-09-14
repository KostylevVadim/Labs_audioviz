from PIL import Image, ImageChops
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def info(file):
    img = Image.open(file)
    width = img.size[0]
    height = img.size[1]
    weight_black, normal_black, x_center, y_center = 0,0,0,0
    for i in range(width):
        for j in range(height):
            if img.getpixel((i,j))[0] == 0 and img.getpixel((i,j))[1] == 0 and img.getpixel((i,j))[2] == 0:
                weight_black += 1
                x_center += i
                y_center += j
    size = width * height
    weight_1, weight_2, weight_3, weight_4 = 0, 0, 0, 0
    for i in range(width//4):
        for j in range(height//4):
            weight_1+=1
    
    for i in range(width//4, width):
        for j in range(height//4):
            weight_2+=1
    
    for i in range(width//4, width):
        for j in range(height//4, height):
            weight_3+=1
    
    for i in range(width//4):
        for j in range(height//4, height):
            weight_4+=1
    weight_full = 0
    for i in range(width):
        for j in range(height):
            weight_full+=1
    
    normal_black = weight_black / (size)
    x_center = x_center / weight_black
    x_norm_center = (x_center - 1) / (width - 1)
    y_center = y_center / weight_black
    y_norm_center = (y_center - 1) / (height - 1)

    x_moment, x_norm_moment, y_moment, y_norm_moment, diag_45_center, diag_135_center = (
        0,
        0,
        0,
        0,
        0,
        0,
    )
    for i in range(width):
        for j in range(height):
            if img.getpixel((i, j))[0] == 0 and img.getpixel((i, j))[1] == 0 and img.getpixel((i, j))[2] == 0:
                x_moment += (j - y_center) ** 2
                y_moment += (i - x_center) ** 2
                diag_45_center += ((j - y_center - i + x_center) ** 2) / 2
                diag_135_center += ((j - y_center + i - x_center) ** 2) / 2

    x_norm_moment = x_moment / (weight_black ** 2)
    y_norm_moment = y_moment / (weight_black ** 2)
    diag_45_center_rel = diag_45_center / (weight_black ** 2)
    diag_135_center_rel = diag_135_center / (weight_black ** 2)

    return [
        weight_1,
        weight_2,
        weight_3,
        weight_4,
        normal_black,
        x_norm_center,
        y_norm_center,
        x_norm_moment,
        y_norm_moment,
        diag_45_center_rel,
        diag_135_center_rel,
        #weight_full
    ]

def lab5():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    content = os.listdir(SOURE_DIR)
    file_xls = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\data.xls'
    
    s="𐎀𐎁𐎂𐎃𐎄𐎅𐎆𐎇𐎈𐎉𐎊𐎋𐎌𐎍𐎎𐎏𐎐𐎑𐎒𐎓𐎔𐎕𐎖𐎗𐎘𐎙𐎚𐎛𐎜𐎝"
    df = pd.DataFrame({
        'letter':[],
        'weight_1':[],
        'weight_2':[],
        'weight_3':[],
        'weight_4':[],
        
        'normal_black':[],
        'x_norm_center':[],
        'y_norm_center':[],
        'x_norm_moment':[],
        'y_norm_moment':[],
        'diag_45_center_rel':[],
        'diag_135_center_rel':[]
    }) 
    for i in range(len(content)):
        file = SOURE_DIR+str(i)+'.bmp'
        inf = info(file)
        df_temp = pd.DataFrame({
        'letter':[s[i]],
        'weight_1':[inf[0]],
        'weight_2':[inf[1]],
        'weight_3':[inf[2]],
        'weight_4':[inf[3]],
        'normal_black':[inf[4]],
        'x_norm_center':[inf[5]],
        'y_norm_center':[inf[6]],
        'x_norm_moment':[inf[7]],
        'y_norm_moment':[inf[8]],
        'diag_45_center_rel':[inf[9]],
        'diag_135_center_rel':[inf[10]]
    })
        
        df = df.append(df_temp, ignore_index = True )
    
    print(df)
    df.to_excel(file_xls, 'Sheet1')
    #df.save()