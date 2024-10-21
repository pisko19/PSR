import cv2

def main():
    # Start video capture (0 usually refers to the default webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read the frame.")
            break

        # Flip the image horizontally
        frame = cv2.flip(frame, 1)

        # Resize the frame to desired width while maintaining aspect ratio
        desired_width = 500
        aspect_ratio = frame.shape[0] / frame.shape[1]
        new_height = int(desired_width * aspect_ratio)
        frame_resized = cv2.resize(frame, (desired_width, new_height))

        # Create a window without borders
        cv2.namedWindow('Camera Feed', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Camera Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

        # Resize the window to fit the image
        cv2.resizeWindow('Camera Feed', desired_width, new_height)

        # Show the frame in the window
        cv2.imshow('Camera Feed', frame_resized)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
