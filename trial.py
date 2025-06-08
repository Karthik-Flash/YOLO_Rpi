import cv2
import os
from datetime import datetime
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

# Read initial frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Folder to save images
save_dir = r"D:\PROJECTS\Pycharm"
os.makedirs(save_dir, exist_ok=True)

while cap.isOpened() and ret:
    # Motion detection
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

                # Get bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box with label
                cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame2, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                # Save frame if "bottle" or "cell phone" detected
                if label in ["bottle", "cell phone"] and not detected:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = os.path.join(save_dir, f"{label}_{timestamp}.jpg")
                    cv2.imwrite(filename, frame2)
                    print(f"✅ Detected {label}. Image saved at: {filename}")
                    detected = True  # Avoid multiple saves in one frame

    # Show live webcam with drawings
    cv2.imshow("Live Feed", frame2)

    # Prepare for next loop
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
