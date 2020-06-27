class RingBuffer:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.oldest = 0

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.oldest] = item
            self.oldest += 1
        if self.oldest == self.capacity:
            self.oldest = 0

    def get(self):
        return self.items