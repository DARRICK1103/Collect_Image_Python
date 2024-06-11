import cv2
import os
import uuid
import time

def capture_images(delay=1):
    # Initialize the webcam
    cap = cv2.VideoCapture(1)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Couldn't open the webcam.")
        return

    # Create the directory if it doesn't exist
    directory = os.path.join("flask_app", "data", "valid")
    os.makedirs(directory, exist_ok=True)

    # Flag to control image capturing
    capturing = False

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow("Press 'w' to start capturing, 'p' to pause, 'q' to quit", frame)

        # Listen for key press
        key = cv2.waitKey(1)

        # If 'q' is pressed, quit the loop
        if key == ord('q'):
            break

        # If 'w' is pressed, start capturing images
        if key == ord('w'):
            capturing = True
            print("Start capturing...")

        # If 'p' is pressed, pause capturing
        if key == ord('p'):
            capturing = False
            print("Pause capturing...")

        # Capture images if capturing is True
        if capturing:
            # Generate a unique filename
            unique_name = str(uuid.uuid4())
            filename = os.path.join(directory, f"{unique_name}.jpg")

            # Save the captured image
            cv2.imwrite(filename, frame)
            print("Image captured and saved as:", filename)

            # Introduce delay
            time.sleep(delay)

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images(delay=0.5)  # Change the delay time as needed, in seconds
