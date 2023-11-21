import cv2
import numpy as np
import streamlit as st

def enhance_image(image, contrast_factor, brightness_factor, smoothing_kernel_size, sharpening_factor, mask_image, morph_operation):
    # Adjust contrast and brightness
    enhanced_image = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=brightness_factor)

    # Smoothening
    if smoothing_kernel_size > 0:
        enhanced_image = cv2.GaussianBlur(enhanced_image, (smoothing_kernel_size, smoothing_kernel_size), 0)

    # Sharpening
    if sharpening_factor > 0:
        kernel = np.array([[-1, -1, -1],
                           [-1, 9 + sharpening_factor, -1],
                           [-1, -1, -1]])
        enhanced_image = cv2.filter2D(enhanced_image, -1, kernel)

    # Masking
    if mask_image is not None:
        mask_image = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask_image, 30, 255, cv2.THRESH_BINARY)
        enhanced_image = cv2.bitwise_and(enhanced_image, enhanced_image, mask=mask)

    # Morphological operations
    if morph_operation == 'Dilation':
        kernel = np.ones((5, 5), np.uint8)
        enhanced_image = cv2.dilate(enhanced_image, kernel, iterations=1)
    elif morph_operation == 'Erosion':
        kernel = np.ones((5, 5), np.uint8)
        enhanced_image = cv2.erode(enhanced_image, kernel, iterations=1)

    return enhanced_image

# Streamlit UI
st.title("Image Enhancement App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = cv2.imread(uploaded_file.name)

    st.subheader("Original Image")
    st.image(image, channels="BGR")

    # User input for enhancement parameters
    contrast_factor = st.slider("Contrast", 0.5, 2.0, 1.0)
    brightness_factor = st.slider("Brightness", -50, 50, 0)
    smoothing_kernel_size = st.slider("Smoothing Kernel Size", 0, 15, 0)
    sharpening_factor = st.slider("Sharpening", 0, 5, 0)

    mask_image = st.file_uploader("Upload a mask image (optional)...", type=["jpg", "jpeg", "png"])

    morph_operations = ['None', 'Dilation', 'Erosion']
    morph_operation = st.selectbox("Morphological Operation", morph_operations)

    if st.button("Enhance Image"):
        if mask_image is not None:
            mask_image = cv2.imread(mask_image.name)
        enhanced_image = enhance_image(image, contrast_factor, brightness_factor, smoothing_kernel_size, sharpening_factor, mask_image, morph_operation)

        st.subheader("Enhanced Image")
        st.image(enhanced_image, channels="BGR", use_column_width=True)
