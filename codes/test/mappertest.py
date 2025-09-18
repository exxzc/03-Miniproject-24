from note_mapper import NoteMapper
import time

mapper = NoteMapper([261,293,329,349,392,440,494,523])
test_values = [0.1, 0.2, 0.21, 0.8, 0.82, 0.3, 0.35]
for x in test_values:
    hz = mapper.map_norm_to_hz(x, time.ticks_ms())
    print("norm:", x, "mapped freq:", hz)
    time.sleep(0.05)

