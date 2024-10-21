import argparse
import cv2
import json
import numpy as np
from functools import partial

# Global variable for trackbars
limits = {'limits': {'B': {'min': 0, 'max': 255},
                     'G': {'min': 0, 'max': 255},
                     'R': {'min': 0, 'max': 255}}}

# Mouse callback function
def onTrackbar(value, channel, limit_type, window_name, image, color_space):
    """Callback function to update the min/max limits for each channel."""
    # Update the limits dictionary
    limits['limits'][channel][limit_type] = value

    # Perform segmentation based on updated trackbar values
    segment_image(window_name, image, color_space)

def segment_image(window_name, image, color_space):
    """Function to apply color segmentation based on the trackbar values."""
    # Get the min/max limits for each channel
    min_b = limits['limits']['B']['min']
    max_b = limits['limits']['B']['max']
    min_g = limits['limits']['G']['min']
    max_g = limits['limits']['G']['max']
    min_r = limits['limits']['R']['min']
    max_r = limits['limits']['R']['max']

    if color_space == 'HSV':
        # Convert to HSV
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([min_b, min_g, min_r])
        upper_bound = np.array([max_b, max_g, max_r])
        mask = cv2.inRange(image_hsv, lower_bound, upper_bound)
    else:
        # BGR Mode
        lower_bound = np.array([min_b, min_g, min_r])
        upper_bound = np.array([max_b, max_g, max_r])
        mask = cv2.inRange(image, lower_bound, upper_bound)

    # Apply the mask to the image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Show the result
    cv2.imshow(window_name, result)

def save_limits_to_json():
    """Save the limits to a JSON file."""
    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print(f'Writing limits to file {file_name}')
        json.dump(limits, file_handle)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('--hsv', action='store_true', help='Use HSV color space instead of BGR')
    args = vars(parser.parse_args())

    # Load the image
    image = cv2.imread(args['image'])
    if image is None:
        print(f"Error: Could not load image from {args['image']}")
        return

    height, width = image.shape[:2]
    color_space = 'HSV' if args['hsv'] else 'BGR'
    window_name = 'Color Segmentation'

    # Create a window with a specific size
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)

    # Create trackbars for each channel and limit (min/max)
    for channel, values in limits['limits'].items():
        cv2.createTrackbar(f'{channel} Min', window_name, values['min'], 255,
                           partial(onTrackbar, channel=channel, limit_type='min', window_name=window_name, image=image, color_space=color_space))
        cv2.createTrackbar(f'{channel} Max', window_name, values['max'], 255,
                           partial(onTrackbar, channel=channel, limit_type='max', window_name=window_name, image=image, color_space=color_space))

    # Perform the initial segmentation with default values
    segment_image(window_name, image, color_space)

    # Wait for a key press, and then exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save limits to a JSON file when the program closes
    save_limits_to_json()

if __name__ == '__main__':
    main()
