from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort

MODEL_PATH = Path(__file__).resolve().parents[1] / "yolo" / "weights" / "best.onnx"
CLASSES = ["speed-breaker", "pothole"]
INPUT_SIZE = (640, 640)


def initialize_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap.release()
        raise RuntimeError("Unable to open camera (device index 0).")
    return cap


def load_model():
    return ort.InferenceSession(
        MODEL_PATH,
        providers=["CPUExecutionProvider"],
    )


def preprocess(frame):
    image = cv2.resize(frame, INPUT_SIZE)
    image = image.astype(np.float32) / 255.0
    image = image.transpose(2, 0, 1)  # HWC -> CHW
    return np.expand_dims(image, axis=0)


def detect_objects(session, frame):
    image = preprocess(frame)
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: image})

    # This matches the output-row format assumed in the original script:
    # [x, y, w, h, objectness, class_score_0, class_score_1, ...].
    # Some YOLOv5 ONNX exports need output decoding and NMS instead.
    return outputs[0][0]
