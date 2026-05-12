from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import cv2
import numpy as np
import base64
import time

from ai_pipeline import process_frame

app = FastAPI()
@app.get("/test")
async def test():
    return {"message": "phone can connect"}
app.mount("/static", StaticFiles(directory="static"), name="static")

fps = 0
frame_count = 0
start_time = time.time()


@app.get("/")
async def home():
    with open("static/viewer.html", "r") as f:
        return HTMLResponse(f.read())


@app.get("/sender")
async def sender():
    with open("static/sender.html", "r") as f:
        return HTMLResponse(f.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    global fps
    global frame_count
    global start_time

    await websocket.accept()

    try:
        while True:

            data = await websocket.receive_text()

            header, encoded = data.split(",", 1)

            img_bytes = base64.b64decode(encoded)

            np_arr = np.frombuffer(img_bytes, np.uint8)

            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            processed_frame = process_frame(frame)

            _, buffer = cv2.imencode(".jpg", processed_frame)

            jpg_as_text = base64.b64encode(buffer).decode("utf-8")

            await websocket.send_text(jpg_as_text)

            frame_count += 1

            elapsed = time.time() - start_time

            if elapsed >= 1:
                fps = frame_count
                frame_count = 0
                start_time = time.time()

                print(f"FPS: {fps}")

    except WebSocketDisconnect:
        print("Client disconnected")