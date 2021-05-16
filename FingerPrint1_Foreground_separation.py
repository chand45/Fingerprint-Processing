#======================================================================
# Author - Dr. Manish Kashyap
#======================================================================

# PURPOSE : Foregroung Background separation (Grayscale Fingerprint Images)


import my_package.my_functions as mf # This is a user defined package
import cv2,matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sci
import scipy.fft as sfft
       
#---------------------------------------------------------------------------
#                Importing the image and knowing the shape
#---------------------------------------------------------------------------

input_image=np.float32(cv2.imread('Finger5.jpg',0))
mf.my_imshow(mf.norm_uint8(input_image),'Original Fingerprint Image')
r,c=np.shape(input_image)
print("The number of rows in the image is ... ",r)
print("The number of cols in the image is ... ",c)

#----------------------------------------------------------------------------------
#                       LOWPASS FILTERING
#----------------------------------------------------------------------------------
n=21;
filter1=np.ones([n,n])/(n**2) # Lowpass Filter
filtered_image=sci.correlate(input_image,filter1)
mf.my_imshow(mf.norm_uint8(filtered_image),'Lowpass Filter applied on image')

#----------------------------------------------------------------------------------
#                         MASK CREATION
#----------------------------------------------------------------------------------

mask_image=1*(filtered_image<200)
mf.my_imshow(mf.norm_uint8(mask_image),"CREATED BINARY MASK")



print("Completed Successfully ...")












