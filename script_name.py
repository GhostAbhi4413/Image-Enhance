import streamlit as st
import cv2
import numpy as np

def enhance_image(image, contrast, brightness, smoothing, sharpening, mask):
    # Adjust contrast and brightness
    enhanced_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)

    # Apply smoothing
    if smoothing:
        enhanced_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)

    # Apply sharpening
    if sharpening:
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        enhanced_image = cv2.filter2D(enhanced_image, -1, kernel)

    # Apply masking
    if mask is not None:
        enhanced_image = cv2.bitwise_and(enhanced_image, enhanced_image, mask=mask)

    return enhanced_image

def main():
    st.title("Image Enhancer")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        # Display original image
        st.image(image, caption="Original Image", use_column_width=True)

        # Parameters for image enhancement
        contrast = st.slider("Contrast", 0.0, 3.0, 1.0)
        brightness = st.slider("Brightness", -100, 100, 0)
        smoothing = st.checkbox("Apply Smoothing")
        sharpening = st.checkbox("Apply Sharpening")

        # Upload mask image for masking operation
        mask_file = st.file_uploader("Choose a mask image (optional)...", type=["jpg", "jpeg", "png"])
        mask = None
        if mask_file is not None:
            mask = cv2.imdecode(np.fromstring(mask_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

        # Enhance the image
        enhanced_image = enhance_image(image, contrast, brightness, smoothing, sharpening, mask)

        # Display enhanced image
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)

if __name__ == "__main__":
    main()
