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

Languages
    Python
Libraries
    OpenCV
    Ultralytics YOLOv8
    NumPy
    MSS
    PyGetWindow
Tools
    ADB
    scrcpy
    VS Code

---

## Application

    Smart surveillance systems
    Edge AI research
    Mobile vision systems
    Real-time monitoring
    AI-assisted analytics
    Object tracking systems
