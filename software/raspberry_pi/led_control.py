from gpiozero import OutputDevice

led_start = None
led_detection = None
led_confirm = None


def initialize_leds():
    global led_start, led_detection, led_confirm

    led_start = OutputDevice(5)
    led_detection = OutputDevice(6)
    led_confirm = OutputDevice(26)

    led_start.on()


def detection_led_on():
    if led_detection is not None:
        led_detection.on()


def detection_led_off():
    if led_detection is not None:
        led_detection.off()


def confirmation_led_on():
    if led_confirm is not None:
        led_confirm.on()


def confirmation_led_off():
    if led_confirm is not None:
        led_confirm.off()


def cleanup_leds():
    global led_start, led_detection, led_confirm

    for led in (led_start, led_detection, led_confirm):
        if led is not None:
            led.off()
            led.close()

    led_start = None
    led_detection = None
    led_confirm = None
