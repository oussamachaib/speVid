# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:09:11 2020

@author: oussama.chaib
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:06:45 2020

@author: oussama.chaib
"""

from pylab import*
import spe2py as spe
import spe_loader as sl
import cv2
import os
import abel as ab

close('all')

tic=time.time()

# Image and save path

path = "/Users/oussamachaib/Desktop/"
folder = "Testing Python Codes"+"/"
file = "test"
ext = ".spe"

print("Loading imaging settings...")


# Number of frames per partition
Ni=0
Nf=20
N_img = 20
Np=Nf-Ni+1

# Cropping limits
    # top left
x1 = 0
y1 = 0
    # bottom right
x2 = 1024
y2 = 1024

#Initialization
sum_img = zeros((y2-y1,x2-x1))
avg = zeros((y2-y1,x2-x1))
img_backup=zeros((y2-y1,x2-x1))
img1=zeros((N_img,y2-y1,x2-x1))
print("Loading partition data...")
k = 0


file_object=sl.load_from_files([path+folder+file+ext])
# Reading frames
for j in range(0,N_img):
    print(j)
    frame_data = file_object.data[j]
    img0 = frame_data[0]
    img1[j,:,:] = img0[y1:y2,x1:x2] 

out = cv2.VideoWriter(str(file)+'.mp4',cv2.VideoWriter_fourcc(*'MP4V'),5,(y2-y1,x2-x1),False)

for i in range(N_img):
    out.write(((img1[N_img-i-1,:,:]/img1[N_img-i-1,:,:].max())*255).astype(uint8))
out.release()

