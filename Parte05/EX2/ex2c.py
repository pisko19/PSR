import cv2
import numpy as np

def main():

    image_filename = 'imagens/atlascar2.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load the color image

    # Check if the image is loaded properly
    if image is None:
        print(f"Error: Failed to load image from '{image_filename}'.")
        return

    # 1. Split the image into its three channels: blue, green, and red
    b_channel, g_channel, r_channel = cv2.split(image)

    # 2. Binarize each channel using different thresholds
    _, b_thresh = cv2.threshold(b_channel, 50, 255, cv2.THRESH_BINARY)  # Blue channel binarized with 50
    _, g_thresh = cv2.threshold(g_channel, 100, 255, cv2.THRESH_BINARY)  # Green channel binarized with 100
    _, r_thresh = cv2.threshold(r_channel, 150, 255, cv2.THRESH_BINARY)  # Red channel binarized with 150

    # 3. Stack the three binary channels into one image (merging as RGB)
    merged_image = cv2.merge([b_thresh, g_thresh, r_thresh])

    # 4. Display the original and final merged image for comparison
    cv2.imshow('Original Image', image)
    cv2.imshow('Merged Binarized Image', merged_image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the window when done


if __name__ == '__main__':
    main()
