# YOLO\_RPi

Object detection using YOLO, implemented both on personal computers and on a Raspberry Pi for remote surveillance.

## Overview

This repository presents a vehicle and intrusion detection system built using Ultralytics YOLO and deployed on a Raspberry Pi. It detects motion, identifies objects like people or vehicles, and sends alerts to a monitoring system. For a detailed overview of the system's goals and use cases, see the `AboutProj.md` file in this repository.

This guide is largely inspired by [EJTech's Raspberry Pi YOLO Tutorial](https://www.ejtech.io/learn/yolo-on-raspberry-pi). Follow the steps below to set up your Raspberry Pi and run YOLO models in real-time.

---

## Steps

### 1. Set Up the Raspberry Pi
![image](https://github.com/user-attachments/assets/6dd1fbbb-a113-4ab3-9adf-dfb4c22e353e)

Use Raspberry Pi Imager to flash a 64-bit Raspberry Pi OS (Bookworm) onto an SD card. Boot the Pi with a monitor, keyboard, and internet access.

#### 1a. Update the Raspberry Pi

```bash
sudo apt update
sudo apt upgrade
```

#### 1b. Create a Virtual Environment

```bash
mkdir ~/yolo
cd ~/yolo
python3 -m venv --system-site-packages venv
source venv/bin/activate
```

Reactivate the environment after reboot:

```bash
cd ~/yolo
source venv/bin/activate
```
![image](https://github.com/user-attachments/assets/6003d8d7-1e0f-432e-9f29-a6ffb71511d7)


#### 1c. Install Dependencies

```bash
pip install ultralytics ncnn
```

This might take 10-15 minutes. If it hangs, press Ctrl+C and retry.

#### 1d. Camera Setup

Use a USB webcam (e.g. Logitech c920) or official Raspberry Pi Camera Module 3.

---

### 2. Set Up YOLO Model and Export to NCNN Format

YOLO models in PyTorch (`.pt`) format can be converted to NCNN format for optimized performance on ARM CPUs like the Raspberry Pi.

#### 2a. Download or Transfer a YOLO Model

**Option 1: Pretrained Model**

```bash
yolo detect predict model=yolo11n.pt
```

**Option 2: Custom Trained Model**
Move your `.pt` file into the `~/yolo` directory using USB, SCP, cloud, etc.

#### 2b. Export to NCNN Format

```bash
yolo export model=your_model.pt format=ncnn
```
![image](https://github.com/user-attachments/assets/c48925d6-d572-4d8a-8c62-8319328ade6a)

This creates a folder (e.g., `yolo11n_ncnn_model`) containing the optimized model files.

---

### 3. Run YOLO Model on the Raspberry Pi

Download a basic detection script:

```bash
wget https://ejtech.io/code/yolo_detect.py
```

#### Running the Script

Example command to run with a USB webcam:

```bash
python yolo_detect.py --model=yolo11n_ncnn_model --source=usb0 --resolution=640x480
```

To stop the script, press `q`.
![image](https://github.com/user-attachments/assets/32ba2fa3-a98e-4cab-a5fd-0408a1578080)
![people](https://github.com/user-attachments/assets/87a258ac-1484-4227-aa5b-3e792af1d3d6)
![2people and phone](https://github.com/user-attachments/assets/74631af3-b3b4-4233-b807-eb10ec5f799b)

#### Other Examples:

```bash
python yolo_detect.py --model=yolo11n_ncnn_model --source=test_video.mp4
python yolo_detect.py --model=custom_ncnn_model --source=img_dir
```

#### Troubleshooting:

If you see an error like `Unable to receive frames`, try:

* Reconnecting the camera
* Trying a different port or camera
* Searching online for specific error solutions

---

## Performance Notes

* Achieved \~8 FPS on Raspberry Pi 5 with YOLO11n NCNN.
* Sufficient for motion detection and object recognition in controlled scenarios.
* Works well in daylight or good lighting conditions.

---

## Limitations

* Raspberry Pi 4/5 has limited compute power.
* Real-time performance is possible only with small, optimized models.
* Low frame rate under poor lighting or occlusion.
* Can be improved with a Coral USB Accelerator or more efficient models.

---

## Future Enhancements

* Secure alert transmission via MQTT or HTTPS.
* Use of hardware accelerators (e.g., Google Coral, Intel NCS2).
* Integration with alarm systems and cloud logging.

---

This project proves edge devices can perform intelligent surveillance affordably and effectively. See `AboutProj.md` for complete use-case details.
