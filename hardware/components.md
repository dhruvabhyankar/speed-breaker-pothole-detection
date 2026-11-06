# Hardware Components

## 1. Overview

The Speed Breaker and Pothole Detection and Alarm System uses embedded hardware components, sensors and an alert mechanism to identify road hazards and notify the driver.

The hardware works together with a YOLOv5-based object detection model running on a Raspberry Pi.

## 2. Components List

| Sr. No. | Component | Purpose |
|---|---|---|
| 1 | Raspberry Pi 4 Model B | Main processing unit |
| 2 | USB Webcam | Captures real-time road images |
| 3 | Ultrasonic Sensor (HC-SR04) | Measures distance to detected road hazards |
| 4 | Buzzer | Provides audible alerts |
| 5 | LEDs | Provides visual indications |
| 6 | Battery / Power Supply | Supplies power to the system |
| 7 | Connecting Wires | Establishes electrical connections |

## 3. Component Descriptions

### 3.1 Raspberry Pi 4 Model B

The Raspberry Pi 4 Model B acts as the central processing unit of the project.

**Functions:**
- Processes camera input.
- Runs the YOLOv5 object detection model.
- Communicates with the ultrasonic sensor.
- Controls the buzzer and LED indicators.
- Coordinates the overall system operation.

### 3.2 USB Webcam

The USB webcam is used to capture real-time images of the road ahead.

**Functions:**
- Continuously captures road images.
- Supplies image frames to the Raspberry Pi.
- Provides visual input for pothole and speed breaker detection.

### 3.3 Ultrasonic Sensor (HC-SR04)

The ultrasonic sensor measures the distance to objects using ultrasonic sound waves.

**Functions:**
- Sends ultrasonic pulses.
- Receives reflected signals.
- Calculates distance based on the time taken by the reflected signal.
- Provides distance measurements to the Raspberry Pi.

### 3.4 Buzzer

The buzzer is an audible alert component.

**Functions:**
- Produces an audible warning when a road hazard is detected and the alert condition is satisfied.
- Alerts the driver to take appropriate precautions.

### 3.5 LEDs

LEDs provide visual indications of system status.

**Functions:**
- Indicate system operation.
- Provide visual warnings when a hazard is detected.
- Help the driver recognize alert conditions.

### 3.6 Battery / Power Supply

The power supply provides the electrical energy required by the system.

**Functions:**
- Powers the Raspberry Pi.
- Supplies power to the connected hardware modules through suitable power connections.

### 3.7 Connecting Wires

Connecting wires establish electrical connections between the Raspberry Pi, sensors and output devices.

**Functions:**
- Connect input and output modules.
- Carry power and signal connections.
- Enable communication between hardware components.

## 4. Hardware Integration

The hardware components are integrated as follows:

1. The USB webcam captures road images.
2. The Raspberry Pi processes the images using the YOLOv5 model.
3. The ultrasonic sensor provides distance measurements.
4. The Raspberry Pi processes the detection and sensor information.
5. The buzzer and LEDs provide alerts to the driver.

## 5. Hardware Notes

- Ensure that the Raspberry Pi receives a suitable regulated power supply.
- The HC-SR04 Echo output is typically 5V and must be level-shifted before connecting to a Raspberry Pi GPIO input.
- Use appropriate current-limiting resistors for LEDs.
- Use a suitable transistor or driver circuit if the buzzer requires more current than a GPIO pin can supply.
- Verify all connections before powering the circuit.

## 6. Conclusion

The combination of the Raspberry Pi, camera, ultrasonic sensor and alert components provides the hardware foundation for the road hazard detection system. These components work together with the machine learning model to detect road hazards and provide timely warnings to the driver.