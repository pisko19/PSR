import cv2
import numpy as np

def main():
    # Load the image
    image_filename = 'imagens/atlas2000_e_atlasmv.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)

    # Check if the image is loaded properly
    if image is None:
        print(f"Error: Failed to load image from '{image_filename}'.")
        return

    # Convert the image from BGR to HSV color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the HSV range for the green box
    lower_bound = np.array([40, 150, 0], dtype=np.uint8)  # Lower bounds for HSV
    upper_bound = np.array([80, 255, 120], dtype=np.uint8)  # Upper bounds for HSV

    # Create a mask using cv2.inRange
    mask = cv2.inRange(image_hsv, lower_bound, upper_bound)

    # Optional: Apply the mask to the original image to see the segmented area
    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image, mask, and segmented image
    cv2.imshow('Original Image', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Segmented Image', segmented_image)
    
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows when done

if __name__ == '__main__':
    main()
