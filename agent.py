'''Plab 2 Gruppe 20'''

from keypad import Keypad
from led_board import LedBoard


class Agent:
    '''Main class Agent for controlling the hele driten'''

    def __init__(self):
        self.keypad = Keypad()
        self.led_board = LedBoard()
        self.cump = ""
        self.cump_old = ""
        self.pass_path = "password.txt"
        self.override = ""
        self.led = [0, 0]  # [led_num, led_dur]
        self.digit = "0"

    def init_passcode_entry(self):
        '''Clear the password buffer (cump), and run startup light sequence'''
        self.cump = ""
        self.led_board.power_up()

    def get_next_signal(self):
        '''Return the override-signal if it is non-blank;
        otherwise query the keypad for the next pressed key.'''
        if self.override != "":
            return self.override
        self.keypad.get_next_signal()
        self.digit = input("> ")
        return self.digit

    def verify_login(self):
        '''Check that the entered password corresponds to the current password
        and save result to override. Then call lighing sequence'''
        if self.cump == self.get_password():
            self.override = "Y"
            self.led_board.correct_password()
            print("correct password")
        else:
            self.override = "N"
        self.cump = ""

    def light_one_led(self):
        '''Light up the LED self.led[0] for self.led[1] seconds'''
        print("Lighting LED", self.led[0], "for", self.led[1], "seconds")

    def get_password(self):
        '''Returns the current password from the password file'''
        with open(self.pass_path, 'r') as file:
            password = file.readline().strip()
            return password

    def set_password(self, password):
        '''Writes the new password to the password file'''
        with open(self.pass_path, 'w') as file:
            file.write(password)

    def a02(self):
        """adds a digit to cump"""
        self.cump += self.digit

    def a04(self):
        """Resets the FSM"""
        self.cump = ""
        self.cump_old = ""
        self.led = [0, 0]  # [led_num, led_dur]
        self.override = ""

    def a05(self):
        '''Reset override and cump'''
        self.override = ""
        self.cump = ""

    def a06(self):
        """Refreshes the FSM
            (ready to start from active)"""
        self.cump = ""
        self.cump_old = ""
        self.led = [0, 0]  # [led_num, led_dur]
        self.override = ""

    def a07(self):
        '''Cache cump in cump_old, reset cump'''
        self.cump_old = self.cump
        self.cump = ""

    def a08(self):
        """Check that cump == cump_old"""
        if self.cump == self.cump_old:
            self.override = "Y"
            self.led_board.correct_password()
        else:
            self.override = "N"

    def a10(self):
        '''Light up led nr x for k seconds'''
        self.led[1] = int(self.cump)
        self.led_board.light_led(self.led[0], self.led[1])

    def a11(self):
        '''Reset cump, cump_old and override and set the new password'''
        self.set_password(self.cump)
        self.cump = ""
        self.cump_old = ""
        self.override = ""

    def a12(self):
        '''Choose led'''
        self.led[0] = int(self.digit)

    def nothing(self):
        '''Does absolutely nothing'''
