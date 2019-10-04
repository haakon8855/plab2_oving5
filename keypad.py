'''Plab 2 Gruppe 20'''

from time import sleep
import RPi.GPIO as GPIO


class Keypad():
    '''Keypad class to handle input from keyboard'''

    def __init__(self):
        self.rows = [18, 23, 24, 25]
        self.cols = [17, 27, 22]
        self.keypad = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"]
        ]

    def setup(self):
        '''Set up the input and output pins'''
        GPIO.setmode(GPIO.BCM)
        for rowp in self.rows:
            GPIO.setup(rowp, GPIO.OUT)
        for colp in self.cols:
            GPIO.setup(colp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        '''Polls the keyboard and checks which key is pressed'''
        row, col = -1, -1
        correct_input = True
        for rowp in self.rows:
            GPIO.output(rowp, GPIO.HIGH)
            for colp in self.cols:
                if GPIO.input(colp) == GPIO.HIGH:
                    row, col = rowp, colp
                    for _ in range(19):
                        sleep(10)
                        if GPIO.input(colp) != GPIO.HIGH:
                            correct_input = False
                            break
                    if correct_input:
                        while GPIO.input(colp) == GPIO.HIGH:
                            sleep(2)
                    else:
                        row, col = -1, -1
            GPIO.output(rowp, GPIO.LOW)
        return row, col

    def get_next_signal(self):
        '''Calls self.do_polling until a key is pressed'''
        row, col = -1, -1
        while row == -1 and col == -1:
            row, col = self.do_polling()
        return self.get_symbol(row, col)

    def get_symbol(self, row, col):
        '''Input: row, col.
        Returns the corresponding symbol for the given input'''
        return self.keypad[row][col]
