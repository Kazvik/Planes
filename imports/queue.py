class Queue:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def size(self):
        return len(self._data)

    def clear(self):
        self._data.clear()
