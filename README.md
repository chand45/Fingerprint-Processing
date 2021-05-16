# Fingerprint-Processing

FOREGROUND SEPERATION:
      We create a suitable mask which when applied on an image produces the fingerprint which is seperated from the background. This is done by using a suitable threshold on the value of the pixel. Here, we have used a threshold of 200 and created a binary mask. To remove sharp changes in colour a lowpass filter is applied on the image. The filtered image is then used to create a mask.
      
Noise Removal:
      Usually when fingerprints are collected there will be broken lines, ridges collapsing into each other which account for noise in our fingerprint image. Noise is reduced by using median filtering on the image.Although some features are lost after using the median filter, but the key points like ridge endings and bifurcations are still intact which we can match to identify a fingerprint.
We are going to take a logical AND of binarized input image, binarized filter image to get the final image for singularity detection.

Bifurcation Extraction:
      We create a custom 3x3 filter as shown in the code. Image is passed through this filter resulting in an image with high pixel values where convolution result was found to be maximum. We extract these points which represent bifurcation in our fingerprints.
    
Singularity Detection:
      We use the concept of poincare index to dectect bifurcation points and ridge endings. If the crossing number CN (result after convolving the filter) is 1 then the detected point is a ridge ending. If CN is 3 then the detected point is a bifurcation.
