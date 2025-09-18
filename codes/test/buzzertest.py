from buzzer_player import BuzzerPlayer
import time

b = BuzzerPlayer(pin=16)
notes = [261, 329, 392, 523]  # C4, E4, G4, C5
for f in notes:
    print("playing", f)
    b.note_on(f, 0.6)
    time.sleep(0.5)
b.note_off()

