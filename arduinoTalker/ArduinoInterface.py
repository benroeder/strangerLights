import serial

class ArduinoInterface:
    def __init__(self):
        # TODO: modify to use actual id
        ser=serial.Serial('/dev/ttyACM0', 9600)

    def push_message(self, message):
        self.ser.write(message)