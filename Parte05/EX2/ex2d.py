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

    # Define the RGB range for the green box
    # These values might need to be adjusted based on the actual image
    bmin, gmin, rmin = 0, 70, 0   # Lower bounds for RGB
    bmax, gmax, rmax = 40, 255, 100 # Upper bounds for RGB

    # Create a mask using cv2.inRange
    lower_bound = np.array([bmin, gmin, rmin], dtype=np.uint8)
    upper_bound = np.array([bmax, gmax, rmax], dtype=np.uint8)
    mask = cv2.inRange(image, lower_bound, upper_bound)

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
