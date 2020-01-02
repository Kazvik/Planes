class Queue:
    def __init__(self):
        #initializes a a queue data structure
        self._data = []

    def push(self, item):
        #function that pushes an item in the queue
        self._data.append(item)

    def pop(self):
        #function that pops an item from the queue
        #it returns the first element from the queue and it deletes it
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def size(self):
        #returns the size of the queue
        return len(self._data)

