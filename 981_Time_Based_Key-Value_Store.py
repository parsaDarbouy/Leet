from bisect import bisect_right


class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        entries = self.data[key]
        index = bisect_right(entries, timestamp, key=lambda entry: entry[1]) - 1
        if index < 0:
            return ""
        return entries[index][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)