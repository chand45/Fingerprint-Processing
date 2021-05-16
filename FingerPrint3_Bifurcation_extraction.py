#======================================================================
# Author - Dr. Manish Kashyap
#======================================================================

# PURPOSE : Bifurcation extraction in binary fingerprint images
#             (Requires "pip install scikit-image")


import my_package.my_functions as mf # This is a user defined package
import cv2,matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sci
import scipy.fft as sfft
import skimage.morphology as sk
       
#---------------------------------------------------------------------------
#                Importing the image and knowing the shape
#---------------------------------------------------------------------------

input_image=np.float32(cv2.imread('Finger5.jpg',0)) # Use img15.bmp/Finger3.bmp for testing
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
#                       Bifurcation extraction
#----------------------------------------------------------------------------------

filter1=np.array([[1,0,1],[0,1,0],[0,1,0]])
filtered_image=sci.correlate(thinned_image,filter1)
points_of_bifurcation_image=1*(filtered_image==filtered_image.max())
mf.my_imshow(mf.norm_uint8(points_of_bifurcation_image),"Points of Bifurcation")

#----------------------------------------------------------------------------------
#                            Plotting
#----------------------------------------------------------------------------------

indx_r,indx_c=np.where(points_of_bifurcation_image>0)
fig1,ax1=mf.my_imshow(mf.norm_uint8(thinned_image),"Points detected")
ax1.plot(indx_c,indx_r,'ro')


print("Completed Successfully ...")













