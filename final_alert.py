import cv2
import os
from datetime import datetime
from ultralytics import YOLO

# Load YOLOv8 small model for edge deployment
model = YOLO("yolov8s.pt")

# Start webcam capture
cap = cv2.VideoCapture(0)

# Read initial two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Directory to save alert images
save_dir = "D:\PROJECTS\Pycharm\ResultImages"
os.makedirs(save_dir, exist_ok=True)

# Define alert categories
alert_classes = ["person", "car", "truck", "bus", "motorbike"]

while cap.isOpened() and ret:
    # Compute motion difference
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected = False

    if any(cv2.contourArea(c) > 1000 for c in contours):
        results = model(frame2, verbose=False)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                conf = float(box.conf[0])

                # Bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box
                cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame2, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                # Save alert image
                if label in alert_classes and not detected:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = os.path.join(save_dir, f"{label}_{timestamp}.jpg")
                    cv2.imwrite(filename, frame2)
                    print(f"🚨 ALERT: Detected {label}. Saved at: {filename}")
                    # TODO: Implement alert transmission logic (HTTP/MQTT)
                    detected = True

    # Show feed (optional for Pi)
    cv2.imshow("Live Feed", frame2)

    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
