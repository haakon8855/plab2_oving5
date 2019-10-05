"""Module containing methods used for the LED-board"""

from time import sleep, time
import RPi.GPIO as GPIO


class LedBoard:
    """Class that contains methods for the setup of the LED board
    as well as different light sequences."""
    def __init__(self):
        self.pins = [4, 5, 12]
        self.pin_led_states = [
            [1, 0, -1],  # A, 0 means pin is low, 1 means high, -1 means set to be an input
            [0, 1, -1],  # B
            [-1, 1, 0],  # C
            [1, 0, 1],  # D
            [1, -1, 0],  # E
            [0, -1, 1]  # F
        ]
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        """Method for setting the pins"""
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_led(self, led_number, duration=0.5):
        """Turn on one of the 6 LEDs"""
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)
        sleep(duration)
        self.reset()

    def flash_all_leds(self, k):
        """Flash all 6 LEDs on and off for k seconds."""
        t_end = time() + k  # time returns the current time in seconds
        while time() < t_end:
            for i in range(0, 6):
                self.light_led(i, 0.003)
        # self.reset()

    def twinkle_all_leds(self, k):
        """Turn all LEDs on and off in sequence for k seconds."""
        t_end = time() + k
        while time() < t_end:
            for j in range(0, 3):
                self.light_led(j, 0.3)
            for j in range(3, 6):
                self.light_led(k, 0.3)
        # self.reset()

    def power_up(self):
        """Lighting patterns associated with powering up the system."""
        t_end = time() + 3
        while time() < t_end:
            self.light_led(4, 0.003)
            self.light_led(5, 0.003)

    def power_down(self):
        """Lighting patterns associated with powering down the system."""
        t_end = time() + 3
        while time() < t_end:
            self.light_led(0, 0.003)
            self.light_led(1, 0.003)

    def wrong_password(self):
        """Lighting patterns associated with wrong password entry"""
        t_end = time() + 0.4
        while time() < t_end:
            self.light_led(4, 0.003)
            self.light_led(5, 0.003)
        t_end = time() + 1.5
        while time() < t_end:
            self.light_led(2, 0.003)
            self.light_led(3, 0.003)

    def correct_password(self):
        """Lighting patterns associated with correct password entry"""
        t_end = time() + 1
        while time() < t_end:
            self.light_led(4, 0.003)
            self.light_led(5, 0.003)

    def reset(self):
        """Method for resetting all the LEDs"""
        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)
