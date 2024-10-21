import argparse
import cv2
import numpy as np

# Global variables
window_name = 'Thresholding - Exercise 3a'
image_gray = None

def onTrackbar(threshold):
    """Callback function for the trackbar to apply the threshold."""
    # Apply the threshold to the grayscale image
    _, thresholded_image = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    # Show the thresholded image in the window
    cv2.imshow(window_name, thresholded_image)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # Load the image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray  # Use global variable
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert BGR to gray image (single channel)
    
    # Create a window
    cv2.namedWindow(window_name)

    # Create a trackbar for thresholding, default value is set to 127
    cv2.createTrackbar('Threshold', window_name, 127, 255, onTrackbar)

    # Call the callback function once to display the initial thresholding
    onTrackbar(127)

    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows when done

if __name__ == '__main__':
    main()
