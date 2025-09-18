from sensor_hal import SensorHAL
from note_mapper import NoteMapper
from buzzer_player import BuzzerPlayer
import time

s = SensorHAL(vmin=8000, vmax=58000); s.warmup()
m = NoteMapper([261,293,329,349,392,440,494,523])
b = BuzzerPlayer(pin=16)

while True:
    x = s.read_norm()
    hz = m.map_norm_to_hz(x, time.ticks_ms())
    b.note_on(hz, 0.6)
    print("x:", round(x,2), "hz:", hz)
    time.sleep(0.2)
