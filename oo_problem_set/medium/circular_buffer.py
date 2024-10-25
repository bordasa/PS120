class CircularBuffer:
    def __init__(self, num_of_items):
        self._items = []
        self.limit = num_of_items

    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self, limit):
        if not isinstance(limit, int):
            raise ValueError("Buffer size must be an integer.")
        
        self._limit = limit

    def put(self, value):
        if len(self._items) < self.limit:
            self._items.append(value)
        else:
            self._items.pop(0)
            self._items.append(value)
    
    def get(self):
        if not self._items:
            return None

        return self._items.pop(0)

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True