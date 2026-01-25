def handle_command(self, message):
 match message:
    case ['BEEPER', frequency, times]: # Match any message with a string "BEEPER" followed by two other arguments
        self.beep(times, frequency)
    case ['NECK', angle]: # Match any message with a string "NECK" followed by one other argument
        self.rotate_neck(angle)
    case [str(name), _, _, (float(lat), float(lon))]: # Example of pattern matching by type
        print("Yes")
    case [str(name), *_, (float(lat), float(lon))]: # Type + any number of field in the middle
        print("OK")
    case [name, _, _, (lat, lon)] if lon <= 0: # If evaluated only if the pattern matches
        print("Why not")
