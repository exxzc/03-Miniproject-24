# note_mapper.py — map normalized light to frequency with hysteresis
class NoteMapper:
    def __init__(self, hz_scale, hysteresis=0.10, min_hold_ms=180):
        self.scale = hz_scale[:]
        self.hyst = hysteresis
        self.min_hold = min_hold_ms
        self.last_idx = -1
        self.last_change = 0

    def set_scale(self, hz_list): self.scale = hz_list[:]
    def set_hysteresis(self, h):  self.hyst = h
    def set_min_hold(self, ms):   self.min_hold = ms

    def map_norm_to_hz(self, x, now_ms):
        n = len(self.scale)
        seg = 1.0 / n
        idx = min(int(x / seg), n-1)

        # hold note for at least min_hold_ms
        if self.last_idx >= 0 and (now_ms - self.last_change) < self.min_hold:
            return self.scale[self.last_idx]

        # one-step hysteresis
        if self.last_idx >= 0 and abs(idx - self.last_idx) == 1:
            center_last = (self.last_idx + 0.5) * seg
            if abs(x - center_last) < self.hyst * seg:
                idx = self.last_idx

        if idx != self.last_idx:
            self.last_idx = idx
            self.last_change = now_ms
        return self.scale[idx]
