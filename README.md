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

---

##  Android Setup

To get the environment running, ensure your device is configured with the following steps:

### 1. Enable Developer Options
- [ ] Open **Settings** on your Android device.
- [ ] Navigate to **About Phone**.
- [ ] Locate the **Build Number** and tap it **7 times** until you see a message saying "You are now a developer!"

### 2. Enable USB Debugging
- [ ] Go back to the main **Settings** menu.
- [ ] Navigate to **System** > **Developer Options** (or search for it in Settings).
- [ ] Find **USB Debugging** and toggle the switch to **On**.
- [ ] When prompted "Allow USB debugging?", tap **OK**.

---

## Future Improvements

Planned enhancements to expand the system's capabilities:

| Category | Features |
| :--- | :--- |
| **Backend & UI** | FastAPI Integration • Browser Dashboard • WebSocket Streaming • MongoDB Storage |
| **Advanced Vision** | Multi-Object Tracking • OCR Integration • Face & Activity Recognition |
| **Optimization** | GPU Acceleration • Edge TPU (Coral) Support • Video Recording |
| **System Logic** | Real-time Alert Systems • Advanced Detection Analytics |

---

## Performance & Optimizations

### Current Optimizations
- [x] **Dynamic Window Tracking:** Only captures the targeted application window.
- [x] **Region-Based Capture:** Focuses on specific ROIs to reduce processing load.
- [x] **Inference:** Currently utilizing the lightweight `YOLOv8n` (Nano) model.
- [x] **Monitoring:** Real-time FPS overlay for performance benchmarking.

### Planned Optimizations
- [ ] **Parallel Processing:** Moving to Threaded Inference and Asynchronous pipelines.
- [ ] **Hardware Acceleration:** Implementing **CUDA** for NVIDIA GPUs.
- [ ] **Model Compression:** Leveraging **TensorRT** for high-speed inference on edge devices.

---
