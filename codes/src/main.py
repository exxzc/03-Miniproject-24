# main.py — Modular Light Orchestra (no Wi-Fi)
from sensor_hal import SensorHAL
from note_mapper import NoteMapper
from buzzer_player import BuzzerPlayer
import time

# ====== Config (identical behavior to your working script) ======
VMIN = 8000       
VMAX = 58000      
AVG_WINDOW = 8
HYST = 0.10
MIN_HOLD_MS = 180
SAMPLE_DT_MS = 10

# C major: C4..C5 (Hz)
C_MAJOR = [261, 293, 329, 349, 392, 440, 494, 523]

def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x

def main():
    # A: Sensor
    sensor = SensorHAL(adc_pin=28, avg_window=AVG_WINDOW, vmin=VMIN, vmax=VMAX)
    sensor.warmup()

    # B: Mapper
    mapper = NoteMapper(hz_scale=C_MAJOR, hysteresis=HYST, min_hold_ms=MIN_HOLD_MS)

    # C: Player
    player = BuzzerPlayer(pin=16)

    print("Light->Music (modular, fixed VMIN/VMAX). Adjust VMIN/VMAX if needed.")
    last_log = 0
    current_freq = 0
    last_note_ms = 0

    while True:
        now = time.ticks_ms()
        x = sensor.read_norm()
        freq = mapper.map_norm_to_hz(x, now)
        duty = clamp(0.45 + 0.45*x, 0.0, 1.0)

        if current_freq == 0:
            current_freq = freq
            last_note_ms = now
            player.note_on(current_freq, duty)
        else:
            if time.ticks_diff(now, last_note_ms) >= MIN_HOLD_MS and freq != current_freq:
                current_freq = freq
                last_note_ms = now
            player.note_on(current_freq, duty)

        if time.ticks_diff(now, last_log) > 200:
            last_log = now
            print("norm=", round(x,3), "freq=", current_freq, "duty=", round(duty,2))

        time.sleep_ms(SAMPLE_DT_MS)

main()

