import cv2
import numpy as np
import mss
import pygetwindow as gw
import time
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Find scrcpy window
target_window = None

for title in gw.getAllTitles():

    if "SM-" in title or "scrcpy" in title:
        windows = gw.getWindowsWithTitle(title)

        if len(windows) > 0:
            target_window = windows[0]
            break

if target_window is None:
    print("scrcpy window not found")
    exit()

# Maximize window
try:
    target_window.restore()
    target_window.activate()
except:
    pass

time.sleep(1)

print("Connected to:", target_window.title)

sct = mss.mss()

prev_time = 0

while True:

    # Dynamically get exact scrcpy window coordinates
    left = target_window.left
    top = target_window.top
    width = target_window.width
    height = target_window.height

    monitor = {
        "top": top,
        "left": left,
        "width": width,
        "height": height
    }

    # Capture scrcpy window only
    screenshot = sct.grab(monitor)

    frame = np.array(screenshot)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    # Resize for stable inference
    frame = cv2.resize(frame, (480, 900))

    # YOLO inference
    results = model(frame)

    annotated = results[0].plot()

    # FPS calculation
    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    cv2.putText(
        annotated,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Bigger output window
    cv2.namedWindow("EdgeVision AI", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("EdgeVision AI", 500, 950)

    cv2.imshow("EdgeVision AI", annotated)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()