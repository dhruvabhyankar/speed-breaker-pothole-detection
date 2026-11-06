import time
from gpiozero import OutputDevice

buzzer = None


def initialize_buzzer():
    global buzzer
    buzzer = OutputDevice(25)


def trigger_alarm(duration_seconds=1.0):
    if buzzer is None:
        raise RuntimeError("Buzzer has not been initialized.")

    buzzer.on()
    try:
        time.sleep(duration_seconds)
    finally:
        buzzer.off()


def cleanup_buzzer():
    global buzzer
    if buzzer is not None:
        buzzer.off()
        buzzer.close()
        buzzer = None
