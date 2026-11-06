from gpiozero import DistanceSensor

sensor = None


def initialize_ultrasonic():
    global sensor
    sensor = DistanceSensor(
        echo=24,
        trigger=23,
        max_distance=2.0,
    )


def get_distance():
    if sensor is None:
        raise RuntimeError("Ultrasonic sensor has not been initialized.")
    return round(sensor.distance * 100, 2)


def cleanup_ultrasonic():
    global sensor
    if sensor is not None:
        sensor.close()
        sensor = None
