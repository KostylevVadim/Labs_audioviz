from PIL import Image, ImageChops
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lab2.lab2 import Bradley_Rot
from lab6.lab6 import get_prof, reference_image
from lab5.lab5 import info
def Segmantization_new(img):
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
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\lettersfromstring/'
    #print(img.size[0],img.size[1])
    for i in range(len(res)):
        left, right = res[i]
        
        #print(left, 0,right)
        new_img = img.crop((left, 0, right+1, img.size[1]-1))
        #print(new_img.size)
        new_img = reference_image(new_img)
        #print(new_im.size)
        new_img.save(SOURE_DIR+ str(i) + ".bmp", mode="1")
    
    return res


def lab7():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\strings/'
    s = '𐎀𐎁𐎂𐎃𐎄𐎅𐎆𐎇𐎈𐎉𐎊𐎋𐎌𐎍𐎎𐎏𐎐𐎑𐎒𐎓𐎔𐎕𐎖𐎗𐎘𐎙𐎚𐎛𐎜𐎝'
    content = os.listdir(SOURE_DIR)
    #print(content)
    ##name = input()
    img = Image.open(SOURE_DIR+"string1.bmp")
    a = int(img.size[0])
    b = int(img.size[1])
    #print("Размер png на входе:",a,b)
    img = Bradley_Rot(img,0.1)
    Segmantization_new(img)
    SOURE_DIR_alfabet = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\image_new\\'
    content = os.listdir(SOURE_DIR_alfabet)
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
        'diag_135_center_rel':[],
        #'weight_full':[]
    })
    list_of_dat = [] 
    for i in range(0,len(content)-1):
        
        file = SOURE_DIR_alfabet+str(i)+'.bmp'
        #print(file)
        inf = info(file)
        list_1 = [s[i],inf[4],inf[5],inf[6],inf[7],inf[8],inf[9],inf[10]]
        list_of_dat.append(list_1)
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
        'diag_135_center_rel':[inf[10]],
        #'weight_full':[inf[11]]
    })
        df = df.append(df_temp, ignore_index = True )
        
    #print(df)
    #print(list_of_dat)
    SOURE_DIR_alfabet = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\lettersfromstring\\'
    content = os.listdir(SOURE_DIR_alfabet)
    df1 = pd.DataFrame({
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
        'diag_135_center_rel':[],
        #'weight_full':[]
    })
    s = '𐎀𐎁𐎂𐎃𐎄𐎅𐎆𐎇𐎈𐎉𐎊𐎋𐎌𐎍𐎎𐎏𐎐𐎑𐎒𐎓𐎔𐎕𐎖𐎗𐎘𐎙𐎚𐎛𐎜𐎝'
    s1 = '𐎒𐎔𐎗𐎔𐎍𐎎𐎍𐎑𐎌𐎁𐎐𐎊'
    list_of_dat_new = [] 
    for i in range(len(content)):
        file = SOURE_DIR_alfabet+str(i)+'.bmp'
        inf = info(file)
        #print(s1[i],inf)
        list_1 = [s1[i],inf[4],inf[5],inf[6],inf[7],inf[8],inf[9],inf[10]]
        list_of_dat_new.append(list_1)
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
        'diag_135_center_rel':[inf[10]],
        #'weight_full':[inf[11]]
    })
        df1 = df.append(df_temp, ignore_index = True )
    #print(df1)
    print(len(list_of_dat_new))
    for i in range(len(list_of_dat_new)):
        el = list_of_dat_new[i][0]
        ro = []
        print(i, el) 
        for j in range(len(list_of_dat)):
            sum1 = 0
            for k in range(1,len(list_of_dat[j])):
                sum1+= (list_of_dat[j][k]-list_of_dat_new[i][k])**2
            #print(list_of_dat[j][0],math.sqrt(sum1))
            ro.append((list_of_dat[j][0],1 - math.sqrt(sum1)))
        res = sorted(ro, reverse=True, key=lambda x: x[1])
        for j in range(7):
            print(res[j][0],res[j][1])
        print('===')
