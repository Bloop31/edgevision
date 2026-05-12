from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")


def process_frame(frame):

    results = model(frame)

    annotated_frame = results[0].plot()

    return annotated_frame