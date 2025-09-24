# Filtering (blurring, smoothing, or noise reduction)
Filtering is a key image processing technique that addresses the problem of noise, which is always present in digital images due to steps like image acquisition, coding, transmission, or processing. 
Filters are used to remove noise while preserving the important details of the image. 
Filters can be selected based on the specific type of noise present (examples of different noises: https://tristanvanleeuwen.github.io/IP_and_Im_Lectures/_images/image_processing_2_0.png). 
To perform image blurring, we transform the original image (the original array) by scanning a filter or kernel (also an array) throughout the original image. 
This process is called convolution. 
Convolution and filtering are quickly explained in this 5-minute YouTube video: https://www.youtube.com/watch?v=6v8dNtknOSM.     

1. Mean filter: A simple sliding window where the center pixel value is replaced with the average of all pixel values within the window (kernel/filter). Application: Reduce Poisson noise. 

2. Median filter: A sliding window where the center pixel value is replaced with the median of all pixel values in the window. Application: Reduce salt and pepper noise. 

3. Gaussian filter: This filter blurs the image using a Gaussian function (based on Gaussian or normal distribution). It is widely used to reduce image noise and reduce detail. Application: Reduce Gaussian noise. 

4. Bilateral filter: This filter uses a Gaussian function but includes an additional multiplicative component based on the difference in pixel intensity. This critical feature ensures that only pixels with similar intensity to the central pixel are included in the calculation, which helps the filter preserve edges while reducing noise.

# Thresholding
Thresholding is a fundamental and often simple technique used in image processing to separate objects of interest (foreground) from the background.
Process:
1. Convert to grayscale: If the input image is color (RGB), it is typically converted to grayscale, as thresholding usually operates on a single channel.
2. Choose a threshold value: This value determines the cutoff point. It can be chosen manually or automatically.
3. Apply the threshold: Each pixel's intensity is compared to the threshold value:
- If the pixel intensity is greater than or equal to the threshold, it is assigned to the foreground (typically white, 255).
- If the pixel intensity is less than the threshold, it is assigned to the background (typically black, 0). 
4. Generate Binary Image: The output is a binary image where the foreground is distinctly separated from the background.

Types of Thresholding:
- Global thresholding: A single threshold value is applied to the entire image.
- Adaptive thresholding: The threshold value is calculated for smaller, localized regions of the image, making it useful for images with varying lighting conditions.

# Morphological operations
Morphological operations are image-processing techniques that focus on analyzing and manipulating the shape and structure (or form) of objects within an image, rather than single pixels.
These operations are particularly useful for tasks like object detection, noise removal, and image segmentation.
They are normally performed on binary images, though they can be extended to grayscale images.

Key components:
1. Input image: Usually a binary image (foreground pixels are white, background is black), or a grayscale image.
2. Structuring element (or kernel): A small matrix or template that defines the neighborhood of pixels over which the operation is performed. The shape and size of this element highly influence the outcome. Structuring elements can be rectangular, elliptical, or cross-shaped.

Fundamental operations: "Erosion" and "Dilation"

|           | Erosion                                                                                                    | Dilation                                                                                                    |
| ----------| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Action    | Shrinks objects and removes pixels from boundaries. The white region decreases.                            | Expands objects and adds pixels to boundaries. The white region increases.                                  |
| Mechanism | A pixel is set to foreground (1) only if all pixels under the structuring element match the foreground.    | A pixel is set to foreground (1) if at least one pixel under the structuring element matches the foreground.|
| Purpose   | Useful for removing small noise (white noises), detaching connected objects, and stripping away extrusions.| Useful for joining adjacent objects, filling small holes, enhancing features, and repairing breaks.         |

Compound operations (Combinations of "Erosion" and "Dilation"):
- Opening (This operation consists of Erosion followed by Dilation): Remove small objects or noise while preserving the shape and size of larger objects.
This is often done because erosion removes noise but also shrinks the object; dilation restores the object size after noise is gone.
- Closing (This operation consists of Dilation followed by Erosion): Fill small holes and gaps inside the foreground objects or small black points on the object while preserving their overall shape.
- Morphological Gradient (This is the difference between the dilation and the erosion of an image): Highlight the boundaries or edges of objects in the image.



