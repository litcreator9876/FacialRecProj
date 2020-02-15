# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:43:40 2020

@author: Sounmay Mishra
"""

import os
import cv2
import numpy as np
import pickle

def preprocessing(image):
    image = cv2.resize(image,(200,200))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return image 

data_dir = os.path.join(os.getcwd(),'clean_data')
im_dir = os.path.join(os.getcwd(),'images')

data = []
label = []

for i in os.listdir(im_dir):
    image = cv2.imread(os.path.join(im_dir,i))
    image = preprocessing(image)
    data.append(image)
    label.append(i.split('_')[0])

data = np.array(data)
label = np.array(label)

with open(os.path.join(data_dir,'images.p'),'wb') as f:
    pickle.dump(data,f)
with open(os.path.join(data_dir,'label.p'),'wb') as f:
    pickle.dump(data,f)