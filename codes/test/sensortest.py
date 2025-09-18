from sensor_hal import SensorHAL
import time

s = SensorHAL(vmin=8000, vmax=58000)
s.warmup()
for i in range(20):
    raw = s.read_raw()
    norm = s.read_norm()
    print("raw:", raw, "norm:", norm)
    time.sleep(0.2)

