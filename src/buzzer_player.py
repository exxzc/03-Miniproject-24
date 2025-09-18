# buzzer_player.py — simple PWM player
from machine import Pin, PWM

class BuzzerPlayer:
    def __init__(self, pin=16):
        self.pwm = PWM(Pin(pin))
        self.current = -1
        self.note_off()

    def note_on(self, freq_hz, duty01=0.6):
        duty01 = 0.0 if duty01 < 0 else (1.0 if duty01 > 1.0 else duty01)
        if freq_hz <= 0 or duty01 <= 0:
            self.note_off()
            return
        freq_hz = int(freq_hz)
        if freq_hz != self.current:
            self.current = freq_hz
            self.pwm.freq(self.current)
        self.pwm.duty_u16(int(65535 * duty01))

    def note_off(self):
        self.pwm.duty_u16(0)
        self.current = -1
