# What is an image?
A digital image is a two-dimensional matrix or array of pixels (picture elements), where each pixel has a specific numerical value representing its intensity or color at a given spatial coordinate.
In a grayscale image, each pixel is coded by 1 byte or 8 bits. 
However, in a color image (RGB image), each pixel is coded by 3 bytes or 24 bits as the stack of 3 color channels (Red, Green and Blue). 
Each color channel (R/G/B in color image or black/while in grayscale image) has integer values from 0 to 255 (in total, 256 values = 2^8).

# What is image processing?
Image processing is a fundamental field that focuses on altering or improving digital images using various methods and tools to transform pixels. 
These transformations are vital as they not only improve aesthetics but also make images more suitable for analysis, especially in biological research. 
Here are examples of how image processing can be applied in biological and medical fields:
- It can help in noise reduction, contrast enhancement, and reconstruction of images in some cases. Therefore, it can enhance the image quality, extracting useful information from microscopy and medical images (MRI, CT scans, X-rays, etc).
- It can be applied to automate some tasks such as objection detection and object counting.
- It can be used to make prediction or classification (often is combined with machine learning).

# Core techniques in image processing 
- Image enhancement: Giving a makeover to an image by brightening dark photos, bringing out hidden details, or making colors pop, thereby making the image more pleasing or informative
- Filtering: Reducing or removing unwanted elements (often referred to as 'noise') from an image, or smoothing rough edges and sharpening blurry parts to highlight important features
- Transformation techniques: Changing the shape or form of an image, such as resizing, rotating, or warping it to fit a specific requirement

# Image processing vs. Computer vision
While image processing (IP) and computer vision (CV) are interconnected and often work together, they have distinct goals.

| Feature      | Image processing                                        | Computer vision                                                                            |
| ------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Primary Goal | To change the image itself by altering and enhancing it | To understand the content of the image and extract meaning                                 |
| Action       | Transforms pixels to improve the quality of raw images  | Teaches computers (models) to interpret visual information and extract meaning from images |
| Example      | Brightening a dark medical scan                         | Teaching a machine (train a model) to recognize a tumor on that scan                       |

Image processing often acts as the essential foundation for computer vision tasks:
- High-quality, well-processed images resulting from IP can significantly enhance the accuracy of CV algorithms.
- Techniques like noise reduction and contrast enhancement performed by IP improve the accuracy of subsequent CV analysis. 
