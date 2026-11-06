# Speed Breaker and Pothole Detection and Alert System

An AI-powered road hazard detection system that identifies potholes and speed breakers using computer vision and ultrasonic sensing, providing real-time alerts to improve road safety.

## Overview

This project combines deep learning and embedded hardware to detect road hazards such as potholes and speed breakers.

The system uses a YOLOv5s object detection model to identify road hazards from camera frames. Once a hazard is detected, an ultrasonic sensor measures its distance. The system then activates a buzzer and visual indicators to alert the driver.

## Key Features

- Real-time pothole detection.
- Speed breaker detection.
- YOLOv5s-based object detection.
- Ultrasonic distance measurement.
- Automatic buzzer alerts.
- LED-based visual indications.
- Raspberry Pi-based embedded processing.

## System Architecture

The system consists of the following major modules:

1. **Processing Unit:** Raspberry Pi 4 Model B.
2. **Vision Module:** Camera for capturing road images.
3. **Machine Learning Module:** YOLOv5s for detecting road hazards.
4. **Distance Measurement:** Ultrasonic sensor.
5. **Alert Module:** Buzzer and LED indicators.
6. **Power Module:** Rechargeable battery system.

## Technologies Used

| Category | Technology |
|---|---|
| Processor | Raspberry Pi 4 Model B |
| Object Detection | YOLOv5s |
| Programming | Python |
| Deep Learning | PyTorch / ONNX |
| Image Processing | OpenCV |
| Camera | OV5647 / USB Webcam |
| Ultrasonic Sensor | US100 / HC-SR04 |
| Alert System | Buzzer and LEDs |
| Operating System | Raspberry Pi OS 64-bit |

## Working Principle

1. The Raspberry Pi initializes the camera, ultrasonic sensor, buzzer and LEDs.
2. The camera continuously captures road images.
3. YOLOv5s processes the captured frames.
4. The model identifies potholes and speed breakers.
5. When a hazard is detected, the yellow LED starts blinking.
6. The ultrasonic sensor measures the distance to the detected hazard.
7. The system evaluates the sensor measurement.
8. When the hazard is confirmed, the buzzer is activated and visual alerts are provided.
9. The system continues monitoring the road.

## Machine Learning Model

The project uses YOLOv5s, fine-tuned to detect two categories:

- Speed breakers
- Potholes

The training configuration is provided in `training/dataset.yaml`.

The model was trained using an 80:20 training-validation split for 50 epochs. The trained model was exported to ONNX format for Raspberry Pi inference.

## Dataset Configuration

The dataset contains two classes:

| Class ID | Class Name |
|---|---|
| 0 | speed-breakers |
| 1 | potholes |

The original dataset is not included in this repository.

## Hardware Requirements

- Raspberry Pi 4 Model B
- Camera module / USB Webcam
- Ultrasonic sensor
- Active buzzer
- LEDs
- Battery module
- Connecting wires and supporting electronics

## Software Requirements

- Python
- YOLOv5
- OpenCV
- ONNX Runtime
- Raspberry Pi OS

Refer to `requirements.txt` for the verified software dependencies.

## Results

The project report describes an approximately 85% detection accuracy.

Additional detection examples, performance measurements and prototype photographs will be included in the `results/` directory.

## Applications

- Road safety monitoring
- Intelligent transportation systems
- Driver assistance systems
- Pothole identification
- Speed breaker detection

## Future Scope

- GPS-based hazard location tracking.
- Road hazard data storage.
- Cloud-based monitoring.
- Mobile application integration.
- Improved detection under different weather and lighting conditions.

## Project Documentation

Refer to the `docs/` directory for the project report, research paper, presentation and system diagrams.

## Acknowledgements

Developed as an academic engineering project under the guidance of Prof. Sheetal Pawar at MIT World Peace University, Pune.

## Disclaimer

This is an academic prototype. It is not a certified automotive safety system and should not replace driver attention or established vehicle safety systems.
