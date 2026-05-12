# EdgeVision: Real-Time Mobile Vision Intelligence Platform

## Overview

EdgeVision is a real-time mobile vision intelligence platform that streams an Android device screen over USB and performs live object detection using YOLOv8.

The system integrates Android USB debugging, scrcpy-based screen streaming, OpenCV-based frame processing, and YOLOv8 inference to create a low-latency edge AI pipeline for real-time computer vision applications.

This project demonstrates concepts related to:

- Computer Vision
- Edge AI
- Real-Time Systems
- Android-to-PC Communication
- AI Inference Pipelines
- Dynamic Screen Capture
- Performance Monitoring

---

## Features

- Real-time Android screen streaming via USB
- YOLOv8 object detection
- Dynamic scrcpy window detection
- Live bounding box visualization
- FPS monitoring
- Low-latency inference pipeline
- Automatic window tracking
- Real-time edge AI processing

---

## System Architecture

```text
Android Device
      ↓
USB Debugging (ADB)
      ↓
scrcpy Screen Stream
      ↓
Python Frame Capture
      ↓
YOLOv8 Inference
      ↓
Real-Time Detection Output
```
---

## Tech Stack

### Languages
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Libraries & Frameworks
*   **Computer Vision:** `OpenCV`, `Ultralytics YOLOv8`
*   **Data Analysis:** `NumPy`
*   **Screen Management:** `MSS`, `PyGetWindow`

###  Tools & Software
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![ADB](https://img.shields.io/badge/Android%20Debug%20Bridge-3DDC84?style=for-the-badge&logo=android&logoColor=white)
*   **Mirroring:** `scrcpy`

---

## Application

    Smart surveillance systems
    Edge AI research
    Mobile vision systems
    Real-time monitoring
    AI-assisted analytics
    Object tracking systems
