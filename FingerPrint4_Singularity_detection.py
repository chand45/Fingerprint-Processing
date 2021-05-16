#======================================================================
# Author - Dr. Manish Kashyap
#======================================================================

# PURPOSE : Singularity detection in binary fingerprint images 

import my_package.my_functions as mf # This is a user defined package
import cv2,matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sci
import scipy.fft as sfft
import skimage.morphology as sk
       
#---------------------------------------------------------------------------
#                Importing the image and knowing the shape
#---------------------------------------------------------------------------

input_image=np.float32(cv2.imread('Finger5.jpg',0))
mf.my_imshow(mf.norm_uint8(input_image),'Original Fingerprint Image')
r,c=np.shape(input_image)
print("The number of rows in the image is ... ",r)
print("The number of cols in the image is ... ",c)

#----------------------------------------------------------------------------------
#                           Binarization
#----------------------------------------------------------------------------------

binary_image=1*(input_image<128)
mf.my_imshow(mf.norm_uint8(binary_image),"Binary Fingerprint Image")

#----------------------------------------------------------------------------------
#                             Thinning
#----------------------------------------------------------------------------------
thinned_image = 1*sk.thin(binary_image)
mf.my_imshow(mf.norm_uint8(thinned_image),"Thinned Binary Fingerprint Image")

#----------------------------------------------------------------------------------
#                         Bifurcation extraction
#----------------------------------------------------------------------------------

Singularity_map=0*thinned_image
for i in np.arange(1,r-1,1):
    for j in np.arange(1,c-1,1):
        if thinned_image[i,j]==1:
            closed_loop=thinned_image[[i-1,i-1,i-1,i,i+1,i+1,i+1,i],[j-1,j,j+1,j+1,j+1,j,j-1,j-1]].copy()
            Singularity_map[i,j]=(1/2)*np.sum(np.abs(closed_loop-np.hstack((closed_loop[1:],closed_loop[0]))))

mf.my_imshow(mf.norm_uint8(Singularity_map),"Singularity Map")

#----------------------------------------------------------------------------------
#                         Plotting (On Thinned Image)
#----------------------------------------------------------------------------------

indx_r1,indx_c1=np.where(Singularity_map==1)  # Ridge ending (Shown in RED)
indx_r2,indx_c2=np.where(Singularity_map==3)  # Bifurcation  (Shown in YELLOW)
fig1,ax1=mf.my_imshow(mf.norm_uint8(thinned_image),"Points detected")
ax1.plot(indx_c1,indx_r1,'ro',label="Ridge Endings")
ax1.plot(indx_c2,indx_r2,'yo',label="Bifurcations")
ax1.legend()

#----------------------------------------------------------------------------------
#                            Plotting (On ORIGINAL IMAGE)
#----------------------------------------------------------------------------------

indx_r1,indx_c1=np.where(Singularity_map==1)  # Ridge ending (Shown in RED)
indx_r2,indx_c2=np.where(Singularity_map==3)  # Bifurcation  (Shown in YELLOW)
fig2,ax2=mf.my_imshow(mf.norm_uint8(input_image),"Points detected")
ax2.plot(indx_c1,indx_r1,'ro',label="Ridge Endings")
ax2.plot(indx_c2,indx_r2,'yo',label="Bifurcations")
ax2.legend()



print("Completed Successfully ...")














