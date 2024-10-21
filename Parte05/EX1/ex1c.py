import cv2
import os
import time

def main():

    # Paths to the two atlascar images
    image1_filename = 'imagens/atlascar.png'
    image2_filename = 'imagens/atlascar2.png'

    # Check if the image files exist
    if not os.path.exists(image1_filename):
        print(f"Error: The file '{image1_filename}' does not exist.")
        return

    if not os.path.exists(image2_filename):
        print(f"Error: The file '{image2_filename}' does not exist.")
        return

    # Load the two images
    image1 = cv2.imread(image1_filename, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image2_filename, cv2.IMREAD_COLOR)

    # Check if both images are loaded properly
    if image1 is None:
        print(f"Error: Failed to load image from '{image1_filename}'.")
        return

    if image2 is None:
        print(f"Error: Failed to load image from '{image2_filename}'.")
        return

    # Alternately display the two images in the same window
    while True:
        # Show the first image
        cv2.imshow('Atlascar', image1)
        if cv2.waitKey(3000) == 27:  # 3000 ms (3 seconds), press 'Esc' to exit
            break

        # Show the second image
        cv2.imshow('Atlascar', image2)
        if cv2.waitKey(3000) == 27:  # 3000 ms (3 seconds), press 'Esc' to exit
            break

    # Close the window when done
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
