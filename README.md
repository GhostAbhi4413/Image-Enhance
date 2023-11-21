__Image Enhancement with OpenCV and Streamlit__

This repository contains a Python program that utilizes the OpenCV library for image processing and Streamlit for creating a user-friendly web interface. 

The program enables users to enhance images through various operations, including contrast adjustment, brightness modification, smoothening, sharpening, masking, and morphological operations.

Key Concepts
1. Contrast and Brightness Adjustment:
Contrast Factor: A scaling factor to control the image contrast.
Brightness Factor: A value to adjust the overall brightness of the image.
2. Smoothening and Sharpening:
Smoothing Kernel Size: The size of the Gaussian blur kernel for smoothening.
Sharpening Factor: A parameter for adjusting the strength of the sharpening filter.
3. Masking:
Users can upload a mask image, and the program applies the mask to the enhanced image using bitwise AND operation.
4. Morphological Operations:
Users can choose between dilation and erosion operations:
Dilation: Expands bright regions in the image.
Erosion: Shrinks bright regions in the image.
