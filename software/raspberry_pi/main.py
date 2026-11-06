import cv2
import numpy as np

from camera import initialize_camera, load_model, detect_objects, CLASSES
from ultrasonic import initialize_ultrasonic, get_distance, cleanup_ultrasonic
from buzzer import initialize_buzzer, trigger_alarm, cleanup_buzzer
from led_control import (
    initialize_leds,
    detection_led_on,
    detection_led_off,
    confirmation_led_on,
    confirmation_led_off,
    cleanup_leds,
)

CONFIDENCE_THRESHOLD = 0.2
DISTANCE_THRESHOLD_CM = 50


def main():
    cap = None
    try:
        initialize_leds()
        initialize_buzzer()
        initialize_ultrasonic()

        session = load_model()
        cap = initialize_camera()

        print("Road Hazard Detection System Started")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Warning: unable to read camera frame")
                continue

            detections = detect_objects(session, frame)

            # LEDs reflect detections in the current camera frame.
            detection_led_off()
            confirmation_led_off()

            for detection in detections:
                conf = float(detection[4])
                class_scores = detection[5:]

                if len(class_scores) == 0:
                    continue

                class_id = int(np.argmax(class_scores))
                class_conf = float(class_scores[class_id])

                if (
                    conf > CONFIDENCE_THRESHOLD
                    and class_conf > CONFIDENCE_THRESHOLD
                    and class_id < len(CLASSES)
                ):
                    label = CLASSES[class_id]

                    if label in ("speed-breaker", "pothole"):
                        detection_led_on()
                        print(f"{label} detected by camera")

                        # Ultrasonic measurement is only requested after
                        # a qualifying camera detection in this frame.
                        distance = get_distance()
                        print(f"Distance: {distance:.2f} cm")

                        if distance < DISTANCE_THRESHOLD_CM:
                            confirmation_led_on()
                            print("Hazard confirmed; activating buzzer.")
                            trigger_alarm()

                        break

    except KeyboardInterrupt:
        print("\nStopping system...")
    finally:
        if cap is not None:
            cap.release()
        cleanup_ultrasonic()
        cleanup_buzzer()
        cleanup_leds()
        print("System stopped.")


if __name__ == "__main__":
    main()
