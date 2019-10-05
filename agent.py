'''Plab 2 Gruppe 20'''

# from keypad import Keypad
# from ledBoard import Led_board


class Agent:
    '''Main class Agent for controlling the hele driten'''

    def __init__(self):
        # self.keypad = Keypad()
        # self.led_board = Led_board()
        self.cump = ""
        self.cump_old = ""
        self.pass_path = "password.txt"
        self.override = ""
        self.led = [0, 0]  # [led_num, led_dur]
        self.digit = "0"

    def init_passcode_entry(self):
        '''Clear the password buffer (cump), and run startup light sequence'''
        self.cump = ""
        # TODO: self.led_board.startup()
        print("startup")

    def get_next_signal(self):
        '''Return the override-signal if it is non-blank;
        otherwise query the keypad for the next pressed key.'''
        if self.override != "":
            return self.override
        # self.digit = self.keypad.get_next_signal()
        self.digit = input("> ")
        return self.digit

    def verify_login(self):
        # A3
        '''Check that the entered password corresponds to the current password
        and save result to override. Then call lighing sequence'''
        if self.cump == self.get_password():
            self.override = "Y"
            # TODO: self.led_board.correct_password()
            print("correct password")
        else:
            self.override = "N"
        self.cump = ""

    def light_one_led(self):
        '''Light up the LED self.led[0] for self.led[1] seconds'''
        print("Lighting LED", self.led[0], "for", self.led[1], "seconds")

    def flash_leds(self):
        '''Flash all LEDs'''
        print("Flash all leds")

    def twinkle_leds(self):
        '''Twinkle all LEDs'''
        print("Twinkle all leds")

    def exit_action(self):
        '''Initiate power down light sequence'''
        print("exit")

    def get_password(self):
        '''Returns the current password from the password file'''
        with open(self.pass_path, 'r') as file:
            password = file.readline().strip()
            return password

    def set_password(self, password):
        '''Writes the new password to the password file'''
        with open(self.pass_path, 'w') as file:
            file.write(password)

    def a2(self):
        """adds a digit to cump"""
        self.cump += self.digit

    def a4(self):
        """Resets the FSM"""
        self.cump = ""
        self.cump_old = ""
        self.led = [0, 0]  # [led_num, led_dur]
        self.override = ""

    def a5(self):
        self.override = ""
        self.cump = ""

    def a6(self):
        """Refreshes the FSM
            (ready to start from active)"""
        self.cump = ""
        self.cump_old = ""
        self.led = [0, 0]  # [led_num, led_dur]
        self.override = ""

    def a7(self):
        self.cump_old = self.cump
        self.cump = ""

    def a8(self):
        """Check that cump == cump_old"""
        if self.cump == self.cump_old:
            self.override = "Y"
            # TODO: self.led_board.correct_password()
        else:
            self.override = "N"

    def a10(self):
        self.led[1] = int(self.cump)
        # Make led ligth up for self.led_duration seconds

    def a11(self):
        self.set_password(self.cump)
        self.cump = ""
        self.cump_old = ""
        self.override = ""

    def a12(self):
        self.led[0] = int(self.digit)

    def nothing(self):
        pass
