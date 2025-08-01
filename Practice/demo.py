import os
import cv2
from ultralytics import YOLO

# Set QT platform to XCB for OpenCV compatibility with Sway
os.environ["QT_QPA_PLATFORM"] = "xcb"

# Expand the relative path to the video file
video_path = os.path.expanduser("asset/video1.mp4")

# Initialize video capture
video = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not video.isOpened():
    print(f"Error: Could not open video file at {video_path}")
    exit()

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Check if frame was read successfully
    if not ret:
        print("End of video or failed to read frame")
        break

    # Process the frame with YOLO
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    for result in results:
        if result.boxes is not None:
            for box in result.boxes:
                # Extract bounding box coordinates, confidence, and class
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())

                # Draw bounding box
                cv2.rectangle(
                    frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2
                )
                # Add label with class name and confidence
                cv2.putText(
                    frame,
                    f"{model.names[cls]} {conf:.2f}",
                    (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1,
                )

    # Display the frame
    cv2.imshow("YOLOv8 Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(4000) & 0xFF == ord("q"):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
