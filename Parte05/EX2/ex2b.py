import cv2
import numpy as np

def main():

    image_filename = 'imagens/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image

    # Convert the image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 1. Binarization using OpenCV's threshold function
    _, image_threshold_opencv = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    # Print the type, shape, and data type of the OpenCV thresholded image
    print("OpenCV Thresholded Image Type:", type(image_threshold_opencv))
    print("OpenCV Thresholded Image Shape:", image_threshold_opencv.shape)
    print("OpenCV Thresholded Image Data Type:", image_threshold_opencv.dtype)

    # 2. Binarization using NumPy ndarray comparison
    image_threshold_numpy = image_gray > 128  # This creates a boolean array

    # Print the type, shape, and data type of the NumPy thresholded image
    print("NumPy Thresholded Image Type:", type(image_threshold_numpy))
    print("NumPy Thresholded Image Shape:", image_threshold_numpy.shape)
    print("NumPy Thresholded Image Data Type:", image_threshold_numpy.dtype)

    # Convert the boolean result of NumPy thresholding to uint8 (0 or 255) for display
    image_threshold_numpy = np.uint8(image_threshold_numpy) * 255

    # Display both images for visual comparison
    cv2.imshow('Thresholded Image (OpenCV)', image_threshold_opencv)
    cv2.imshow('Thresholded Image (NumPy)', image_threshold_numpy)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows when done


if __name__ == '__main__':
    main()
