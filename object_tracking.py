import cv2

# --- Configuration ---
# 0 for default webcam, or replace with the path to a video file (e.g., 'video.mp4')
VIDEO_SOURCE = 0 
WINDOW_NAME = "Real-Time Video Stream"

def process_video_stream(source):
    """Initializes and runs a video stream using OpenCV."""
    
    # 1. Initialize VideoCapture
    cap = cv2.VideoCapture(source)

    # Check if the video source was opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video source {source}")
        return

    print("Video stream started. Press 'q' to exit.")
    
    # --- Main Video Loop ---
    while True:
        # 2. Read Frame
        ret, frame = cap.read()

        # If ret is False, we've reached the end of the file or there's an error
        if not ret:
            print("Finished reading video stream.")
            break

        # --- Placeholder for TASK 4 logic ---
        # Here is where you would add:
        # - Object Detection (YOLO/Faster R-CNN)
        # - Drawing Bounding Boxes
        # - Object Tracking (SORT/Deep SORT)
        # -----------------------------------
        
        # 3. Display Frame
        cv2.imshow(WINDOW_NAME, frame)

        # 4. Check for 'q' key press to quit (waitKey returns the key code)
        # The '1' means it waits for 1 millisecond.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 5. Release and cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Video stream closed.")


if __name__ == "__main__":
    process_video_stream(VIDEO_SOURCE)