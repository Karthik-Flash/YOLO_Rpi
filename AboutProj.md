Vehicle and Intrusion Detection System (YOLO & Raspberry Pi)

Introduction
 Modern surveillance systems increasingly rely on computer vision for detecting vehicles and intruders. Our project utilizes Ultralytics YOLO object detection models to identify and track such objects in real time. YOLO (You Only Look Once) is known for its fast and accurate object detection capabilities and is easy to deploy on both laptops and edge devices like the Raspberry Pi. This system was implemented in two stages: Stage 1 on a laptop for development and testing, and 

Stage 2 on a Raspberry Pi for real-world deployment. The Stage 3, final outcome is a security solution that alerts headquarters when an unauthorized vehicle or individual is detected within a restricted area.

Abstract
 The system is built in two phases. In Stage 1, a laptop runs YOLOv8 and YOLOv11 to detect vehicles and people in images, video files, and live webcam input using OpenCV. This stage verifies detection accuracy and supports real-time processing. In Stage 2, a Raspberry Pi 4 Model B with a 720p USB camera continuously runs a lightweight YOLO model. It uses frame-differencing to detect motion and runs YOLO classification only when necessary. If a car or person is detected, the Pi captures the frame and sends it as an alert to a remote monitoring system. The use case mimics a military base scenario where remote perimeter monitoring is crucial for security.
Use Cases (Military Base Monitoring)
 In low-patrol areas such as military bases, our system functions as a Perimeter Intrusion Detection System (PIDS), actively watching over critical access points like gates or hidden roads. By continuously analyzing a camera’s field of view, it identifies the presence of unauthorized personnel or vehicles. Upon detection, it transmits images to the base command center, enabling prompt response to potential intrusions.
Technical Workflow
Stage 1: Laptop Implementation
 On the laptop, we used pre-trained YOLOv8 and YOLOv11 models with OpenCV and Python. The models processed images, video files, and live webcam feeds. A sample script demonstrates how frames are captured from a webcam, processed by YOLO, and annotated with bounding boxes in real time. YOLOv11 was found to be faster than YOLOv8 on CPU while maintaining similar or better accuracy. This stage helped validate the detection capabilities before moving to the hardware-constrained Pi.


Stage 2 and 3: Raspberry Pi Deployment
 The system was then ported to a Raspberry Pi 4 Model B with a 720p USB webcam. The Pi uses frame differencing to detect motion and runs YOLO inference only when motion is detected. If the YOLO model identifies a "car" or "person" in the frame, the image is saved and transmitted to a remote headquarters system. This was simulated with a laptop receiving alerts. The Pi processes only a few frames per second but is sufficient for slow-moving object detection. The alerting system can use simple network protocols such as HTTP or MQTT for communication.

Code overview
This code captures two back-to-back video frames from a webcam and checks for movement using a method called frame differencing. It first converts the image to grayscale (to reduce data), then applies a blur to remove small noise (like light flicker or minor background changes). After this, it highlights areas with noticeable change using thresholding and contour detection, which helps the system detect if something moved in front of the camera.
If motion is detected, the YOLOv8 model is triggered to check if any important object (like a person, car, truck, bus, or motorbike) is present. If such an object is found, the frame is saved with a label and timestamp. This helps alert the user or base station and ensures that even fast-moving objects are captured from multiple angles which are useful for security and surveillance in sensitive areas.
