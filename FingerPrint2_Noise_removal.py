# PURPOSE : Noise Removal from noisy images (Grayscale Fingerprint Images)


import my_package.my_functions as mf # This is a user defined package
import cv2,matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sci
import scipy.fft as sfft
       
#---------------------------------------------------------------------------
#                Importing the image and knowing the shape
#---------------------------------------------------------------------------

input_image=np.float32(cv2.imread('Finger6.png',0)) # Use img15.bmp/Finger3.bmp for testing
mf.my_imshow(mf.norm_uint8(input_image),'Original Fingerprint Image')
r,c=np.shape(input_image)
print("The number of rows in the image is ... ",r)
print("The number of cols in the image is ... ",c)

#----------------------------------------------------------------------------------
#                            MEDIAN FILTERING
#----------------------------------------------------------------------------------

filtered_image=sci.median_filter(input_image,4)
mf.my_imshow(mf.norm_uint8(filtered_image),"Filtered image (INBUILT Median Filter)")


#----------------------------------------------------------------------------------
#                      Binarisation (by thresholding)
#----------------------------------------------------------------------------------

thresh1=20
t1=1*(input_image<thresh1)
t2=1*(filtered_image<thresh1)
t3=1*np.logical_and((input_image<thresh1),(filtered_image<thresh1))

mf.my_imshow(mf.norm_uint8(t1),"Binary version of input image")
mf.my_imshow(mf.norm_uint8(t2),"Binary version of filtered image")
mf.my_imshow(mf.norm_uint8(t3),"Final image")





print("Completed Successfully ...")

