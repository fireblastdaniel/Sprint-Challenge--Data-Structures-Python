class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.insert_posn = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.insert_posn] = item
            if self.insert_posn == self.capacity - 1:
                self.insert_posn = 0
            else:
                self.insert_posn += 1

    def get(self):
        return self.storage