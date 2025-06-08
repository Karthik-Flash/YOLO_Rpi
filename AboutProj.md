# 🚗🚨 Vehicle and Intrusion Detection System (YOLO & Raspberry Pi)

## 📌 Introduction

Modern surveillance systems increasingly rely on computer vision to detect vehicles and intruders. This project uses **Ultralytics YOLO** object detection models to identify and track such objects in real time.

The system is developed in **three stages**:
1. **Stage 1** – Laptop development and testing
2. **Stage 2** – Raspberry Pi deployment
3. **Stage 3** – A complete end-to-end security solution that sends alerts when an unauthorized vehicle or person is detected in a restricted zone.

---

## 🔍 Abstract

The system was built in two phases before final deployment:

- **Stage 1:** On a laptop, we used **YOLOv8** and **YOLOv11** with **OpenCV** to detect vehicles and people from images, videos, and webcam feeds. This phase focused on verifying accuracy and real-time processing.
  
- **Stage 2:** The setup was moved to a **Raspberry Pi 4 Model B** with a 720p USB webcam. It uses **frame differencing** to detect motion and only runs YOLO inference when necessary. If a person or vehicle is found, the Pi captures and sends the frame as an alert.

The system is designed for scenarios like **military bases**, where perimeter monitoring is essential.

---

## 🛡️ Use Case: Military Base Monitoring

In areas with minimal patrol, like remote parts of a military base, the system acts as a **Perimeter Intrusion Detection System (PIDS)**. It keeps watch over gates and hidden paths.

Whenever a vehicle or person enters the frame:
- Motion is detected.
- YOLO classifies the object.
- If unauthorized, an **image alert is sent** to the base headquarters for action.

---

## ⚙️ Technical Workflow

### Stage 1: Laptop Testing
- Tools: **YOLOv8**, **YOLOv11**, **OpenCV**, **Python**
- Tasks:
  - Process webcam feed, video files, and images.
  - Annotate objects with bounding boxes.
- Observations:
  - **YOLOv11** ran faster on CPU than YOLOv8 with similar or better accuracy.
  - Validated system before moving to hardware-constrained Pi.

### Stage 2 & 3: Raspberry Pi Deployment
- Hardware: **Raspberry Pi 4**, **720p USB Webcam**
- Process:
  1. Detect motion using **frame differencing**.
  2. Run YOLO only when motion is detected.
  3. If a car/person is detected, save the image.
  4. Send alert to HQ (simulated using a laptop).
- Communication: **HTTP/MQTT** (lightweight network protocols)
- Frame rate: ~5–10 FPS (sufficient for slow object monitoring)

---

## 🧠 Code Logic (Simplified)

- **Step 1:** Capture two frames from webcam.
- **Step 2:** Convert to grayscale and blur to reduce noise.
- **Step 3:** Use **thresholding + contour detection** to check for motion.
- **Step 4:** If motion is found, trigger YOLO model.
- **Step 5:** If YOLO detects a person/vehicle:
  - Save the frame.
  - Add timestamp + label.
  - Send to HQ for alert.

---

## 🧱 System Architecture
   +------------------------+        +-----------------------+
   | Raspberry Pi + Camera | -----> | HQ Laptop/Command Box |
   |  - Motion Detection    |        |  - Receives Alerts    |
   |  - YOLO Inference      |        |  - Displays/Stores    |
   +------------------------+        +-----------------------+


- **Edge device:** Raspberry Pi runs detection.
- **HQ:** Laptop receives and logs alert images.
- Straightforward data flow: `Camera → Detection → Alert Image → HQ`

---

## ⚠️ Limitations

- **Low frame rate:** Raspberry Pi handles only ~5–10 FPS.
- **Poor lighting/occlusion:** Reduces detection reliability.
- **Hardware limits:** Larger YOLO models may lag.
- **Suggested Upgrades:**
  - Use **hardware accelerators** (e.g., Coral TPU, Intel NCS).
  - Try **smaller YOLO variants** like YOLO-Nano or YOLOv5s.

---

## ✅ Conclusion

This project proves that:
- **Real-time detection** is possible with low-cost edge devices.
- **Accurate object detection** can run on both laptops and Raspberry Pi.
- The system works well in low-traffic, sensitive areas like **military bases**.

Future improvements could include:
- Faster hardware for better frame rates.
- Encrypted alert transmission.
- Cloud logging or dashboard visualization.

---

## 📚 References

1. How to Run YOLO Detection Models on the Raspberry Pi – EJ Technology Consultants  
2. Ultralytics YOLO Documentation  
3. *Perimeter Intrusion Detection by Video Surveillance: A Survey*, MDPI

---

