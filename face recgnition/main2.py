import cv2

# Initialize the video capture object
video = cv2.VideoCapture(0)

# Check if the video capture is successfully opened
if not video.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    # Capture frame-by-frame
    check, frame = video.read()
    
    # Check if the frame was read correctly
    if not check:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow("frame", frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
