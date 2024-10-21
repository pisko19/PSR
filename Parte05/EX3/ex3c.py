import argparse
import cv2
import numpy as np
from functools import partial

# Mouse callback function to print the coordinates when left button is pressed
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Mouse left button clicked at: ({x}, {y})")

def onTrackbar(threshold, image_gray, window_name):
    """Callback function for the trackbar to apply the threshold."""
    # Apply the threshold to the grayscale image
    _, thresholded_image = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    # Show the thresholded image in the window
    cv2.imshow(window_name, thresholded_image)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # Load the image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    if image is None:
        print(f"Error: Could not load image from {args['image']}")
        return

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert BGR to gray image (single channel)
    window_name = 'Thresholding - Exercise 3a'
    
    # Create a window
    cv2.namedWindow(window_name)

    # Set the mouse callback to print coordinates on left click
    cv2.setMouseCallback(window_name, mouse_callback)

    # Use functools.partial to bind additional arguments (image_gray, window_name)
    trackbar_callback = partial(onTrackbar, image_gray=image_gray, window_name=window_name)

    # Create a trackbar for thresholding, default value is set to 127
    cv2.createTrackbar('Threshold', window_name, 127, 255, trackbar_callback)

    # Call the callback function once to display the initial thresholding
    trackbar_callback(127)

    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows when done

if __name__ == '__main__':
    main()
