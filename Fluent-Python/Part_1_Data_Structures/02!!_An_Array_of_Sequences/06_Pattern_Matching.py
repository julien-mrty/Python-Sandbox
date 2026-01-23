def handle_command(self, message):
 match message:
    case ['BEEPER', frequency, times]: # Match any message with a string "BEEPER" followed by two other arguments
        self.beep(times, frequency)
    case ['NECK', angle]: # Match any message with a string "NECK" followed by one other argument
        self.rotate_neck(angle)