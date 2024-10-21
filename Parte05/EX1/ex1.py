import cv2

def main():

    image_filename = 'imagens/atlascar.png'
    image_filename2 = '/home/pedro/Secretária/PSR/Parte05/imagens/atlascar2.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.imshow('window2', image2)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding
    cv2.destroyAllWindows()  # Close the window when done


if __name__ == '__main__':
    main()