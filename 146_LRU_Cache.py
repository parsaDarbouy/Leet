class LinkedTimeline:
    def __init__(self, time, key):
        self.time = time
        self.key = key
        self.next_time = None
        self.previous_time = None


class LRUCache:

    def __init__(self, capacity: int):
        self.root_time = LinkedTimeline(-1, None)
        self.end_timeline = self.root_time
        self.capacity = capacity
        self.cache_data = {}
        self.time = 0
        self.size = 0

    def add_timeline(self, key):
        self.time += 1
        new_time = LinkedTimeline(self.time, key)
        new_time.previous_time = self.end_timeline
        self.end_timeline.next_time = new_time
        self.end_timeline = new_time
        return new_time
    
    def remove_timeline(self, node):
        previous_time = node.previous_time
        next_time = node.next_time
        previous_time.next_time = next_time
        if next_time is not None:
            next_time.previous_time = previous_time
        else:
            self.end_timeline = previous_time

    def delete_oldest_time(self):
        oldest = self.root_time.next_time
        if oldest is None:
            return
        key = oldest.key
        self.remove_timeline(oldest)
        if key is not None:
            self.cache_data.pop(key)
        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.cache_data:
            return -1
        value, old_time = self.cache_data[key]
        self.remove_timeline(old_time)
        new_time = self.add_timeline(key)
        self.cache_data[key] = (value, new_time)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache_data:
            _, old_time = self.cache_data[key]
            self.remove_timeline(old_time)
            new_time = self.add_timeline(key)
            self.cache_data[key] = (value, new_time)
        else:
            if self.size == self.capacity:
                self.delete_oldest_time()
                new_time = self.add_timeline(key)
                self.cache_data[key] = (value, new_time)
                self.size += 1
            else:
               new_time = self.add_timeline(key)
               self.cache_data[key] = (value, new_time)
               self.size += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)