import cv2
import os
import tempfile
import argparse

def capture_image(output_dir):
    """
    Captures a single frame from the default camera and saves it to a temporary file.
    Prints the path of the saved file.
    """
    # Initialize the camera
    # Using 0 for the default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Give the camera a moment to adjust
    for _ in range(30):
        cap.read()

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    if not ret:
        print("Error: Could not read frame from camera.")
        return

    # Create a temporary file to save the image
    file_path = os.path.join(output_dir, "capture.jpg")
    
    # Save the frame as a JPG file
    cv2.imwrite(file_path, frame)

    # Print the path of the saved image to stdout
    print(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture an image and save it to a specified directory.")
    parser.add_argument("--output_dir", default=tempfile.gettempdir(), help="The directory to save the captured image in.")
    args = parser.parse_args()
    
    capture_image(args.output_dir)