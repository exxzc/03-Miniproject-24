# sensor_hal.py — read & normalize (fixed VMIN/VMAX, no drift)
from machine import ADC
import time

class SensorHAL:
    def __init__(self, adc_pin=28, avg_window=8, vmin=8000, vmax=58000):
        self.adc = ADC(adc_pin)
        self.N = avg_window
        self.buf = [0]*self.N
        self.i = 0
        self.sum = 0
        self.vmin = int(vmin)
        self.vmax = int(vmax)

    def begin(self, adc_pin=28):
        self.adc = ADC(adc_pin)

    def warmup(self):
        self.sum = 0; self.i = 0
        for k in range(self.N):
            v = self.adc.read_u16()
            self.buf[k] = v
            self.sum += v
            time.sleep_ms(5)

    def read_raw(self):
        v = self.adc.read_u16()
        self.sum -= self.buf[self.i]
        self.buf[self.i] = v
        self.sum += v
        self.i = (self.i + 1) % self.N
        return self.sum // self.N

    def read_norm(self):
        v = self.read_raw()
        hi = self.vmax if self.vmax > self.vmin else (self.vmin + 1)
        x = (v - self.vmin) / float(hi - self.vmin)
        if x < 0.0: x = 0.0
        if x > 1.0: x = 1.0
        return x
