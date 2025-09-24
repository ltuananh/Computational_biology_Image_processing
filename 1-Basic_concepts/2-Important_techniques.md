# Filtering (blurring, smoothing, or noise reduction)
Filtering is a key image processing technique that addresses the problem of noise, which is always present in digital images due to steps like image acquisition, coding, transmission, or processing. 
Filters are used to remove noise while preserving the important details of the image. 
Filters can be selected based on the specific type of noise present (examples of different noises: https://tristanvanleeuwen.github.io/IP_and_Im_Lectures/_images/image_processing_2_0.png). 
To perform image blurring, we transform the original image (the original array) by scanning a filter or kernel (also an array) throughout the original image. 
This process is called convolution. 
Convolution and filtering are quickly explained in this 5-minute YouTube video: https://www.youtube.com/watch?v=6v8dNtknOSM.     

1. Mean filter: A simple sliding window where the center pixel value is replaced with the average of all pixel values within the window (kernel/filter) -> Application: Filtering Poisson Noise
.
2. Median Filter: A sliding window where the center pixel value is replaced with the Median of all pixel values in the window
.
    ◦ Application: Filtering Salt and Pepper noise
.
3. Gaussian Filter (Gaussian Smoothing): This filter blurs the image using a Gaussian function. It is widely used to reduce image noise and reduce detail
.
4. Bilateral Filter: This filter uses a Gaussian function but includes an additional multiplicative component based on the difference in pixel intensity. This critical feature ensures that only pixels with similar intensity to the central pixel are included in the calculation, which helps the filter preserve edges while reducing noise
.
