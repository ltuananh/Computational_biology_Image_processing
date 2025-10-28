"""
# Image Processing Packages

In Python, there are several libraries that can be used for image processing:
1. OpenCV (Open Computer Vision Library): one of the fastest and most widely used libraries for image processing and computer vision applications, providing around 2500 algorithms to help build models for object detection, image segmentation, etc.
2. Pillow: based on the Python Imaging Library (PIL), it offers several image processing activities such as point operations and filtering.
3. Scikit-Image: a fast & effective library for image processing tasks including filtering, feature detection, segmentation, geometric transformations, color space manipulation, etc.
4. Numpy: a widely used library for machine learning models and can be used in image processing to manipulate pixels and mask pixel values.
5. Matplotlib: a python library known for creating visualizations, but it can also be used to extract information out of the image. Remark: It is not supportive of all file formats.

For our class, we will focus on OpenCV, Numpy and Matplotlib. OpenCV is huge! Lots of documentation is available online (https://docs.opencv.org/4.x/index.html).

To avoid problems due to package installation, in our class, we will use Google Colab notebook. 
"""

# General imports
import cv2                      # OpenCV: a widely used library for image processing and computer vision tasks.
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files  # To upload files in Colab

# Basics tasks
    # Upload the image file to Colab
    uploaded = files.upload()
    img = cv2.imread("image.png")

    # Visualize a color image
    plt.figure(figsize=(6,6))    # Set the figure size
    plt.title("My image")        # Set the title of the plot (optional)
    plt.imshow(img)              # Display the image
    plt.axis("off")              # Turn off axis numbers and ticks (easier to see the image)
    plt.show()                   # Show the image

    # Visualize a grayscale image
    plt.figure(figsize=(6,6))
    plt.imshow(img, cmap='gray')
    plt.axis("off")
    plt.show()

    # Show the image structure
    print(img)

# Color conversion
    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert from BGR to RGB
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Blurring
    blurred = cv2.blur(img,(5,5))                 # Apply average blur with a 5x5 kernel
    blurred = cv2.medianBlur(img, 3)              # Apply median blur with a kernel size of 3
    blurred = cv2.GaussianBlur(img, (15, 15), 0)  # Apply Gaussian blur with a 15x15 kernel and standard deviation of 0
    blurred = cv2.bilateralFilter(img, 9, 75, 75) # Apply bilateral filter with diameter 9, sigmaColor 75, and sigmaSpace 75

# Thresholding
    plt.hist(blurred.ravel(), bins=256, color='gray')                   # Plot histogram of pixel intensities

    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)     # Apply binary thresholding: Above threshold -> 255, below -> 0. Here threshold is 100.
    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV) # Inverse binary thresholding: Above threshold -> 0, below -> 255. Here threshold is 100.

    binary = cv2.bitwise_not(thresh)                                    # Invert the binary image

# Morphological operations
    # Define a 3x3 kernel of ones for morphological operations
    kernel = np.ones((3,3), np.uint8)
    # Perform morphological operations
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)  # Close small holes inside the foreground objects
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2) # Remove small black points on the foreground

# Find connected components
    #What are connected components? Basically, it allows us to detect objects with irregular shapes and sizes based on the pixels’ connectivity to their neighbors.

    # Find connected components in the binary image
    num_labels, labels = cv2.connectedComponents(opened)

    # Find and draw contours of objects
    output = img.copy()                                                                  # Create a copy of the original image to draw contours on
    for label in range(1, num_labels):                                                   # skip background
        mask = (labels == label).astype("uint8") * 255                                   # Create a binary mask for the current connected component
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours of the connected component
        cv2.drawContours(output, contours, -1, (255,0,0), 1)                             # color outlines