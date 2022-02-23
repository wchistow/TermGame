import time


class Clock:
    def __init__(self):
        self.last_time = time.time()
        self.fps = None
        self._sec_per_tick = 0

    def tick(self, fps: int):
        self._sec_per_tick = 1 / fps
        if time.time() - self.last_time < self._sec_per_tick:
            time.sleep(self._sec_per_tick - (time.time() - self.last_time))
        self.last_time = time.time()

    def get_fps(self) -> float:
        """Return a number of frames per second."""
        return round(1 / self._sec_per_tick, 2)
