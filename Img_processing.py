# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:55:25 2018

@author: RC04026
"""

from PIL import Image
from pytesseract import image_to_string
import pandas as pd
#import os
import glob
#import numpy as np
#import cv2
import csv
import re
from selenium.common.exceptions import NoSuchElementException
#claim_df = pd.DataFrame(columns=['Column1','Column2','Column3','Column4','Column5','Column6','Column7','Column8','Column9','Column10','Column11','Column12','Column13','Column14','Column15','Column16','Column17','Column18','Column19' ])



filenames = []
#blnk_img = []

gif_files = glob.glob("*.jpg")
            
for image in gif_files:

    img = Image.open(image)

    nx,ny = img.size
    img_2 = img.resize((int(nx*3), int(ny*3)),Image.BICUBIC)
#    img_2 = img_2(dpi=(520,520))
    imgtxt =  (image_to_string(img_2, lang= 'eng'))
    
    filenames.append(imgtxt)

    
#    blnk_img.append(gif_files)
#        print (imgtxt)
#    length = imgtxt.count('\n')

#    print (length)

#df = pd.DataFrame(data=imgtxt, sep='\n')
#print (df)

#claim_df = []
#for row in imgtxt:
#    claim_df.append(...)
    
#print (claim_df)
#print(filenames)
s = pd.Series(filenames)


s_1 = s.str.split("\n")

#for i in s_1:
#    cll = s_1.str.split(pat = "'Claim Number:', '<")
#col_df = pd.DataFrame(filenames)
#col_df_split = pd.DataFrame(col_df.tolist())

#claim_df = s_1.to_frame()


print(s_1)

#saving the series to a CSV
s_1.to_csv('claim_list.csv', index = False, header = False)
##copying the saved csv to a DF.
#claim_df = pd.DataFrame.from_csv("C:\\Users\\RC04026\\Desktop\\Python_Programs\\AUP\\claim_list.csv")
#print(claim_df)
#col_df.to_csv('claim_list.csv', index = False, header = False)

#removed unawanted lines
