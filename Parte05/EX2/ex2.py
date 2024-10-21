import cv2
import numpy

def main():

    image_filename = 'imagens/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('window', image_gray)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding
    cv2.destroyAllWindows()  # Close the window when done


if __name__ == '__main__':
    main()