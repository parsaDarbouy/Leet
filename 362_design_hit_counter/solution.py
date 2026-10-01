from bisect import bisect_left


class HitCounter:
    def __init__(self):
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        """Record a hit at timestamp (seconds). Several hits may share a timestamp."""
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """Return the number of hits in [timestamp - 299, timestamp]."""
        window_start = timestamp - 299
        first_valid = bisect_left(self.timestamps, window_start)
        return len(self.timestamps) - first_valid
