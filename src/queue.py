import threading


class Queue:

    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def push(self, x):
        self.lock.aquire()
        self.items.append(x)
        self.lock.release()

    def push(self):
        item = None
        self.lock.aquire()
        if len(self.items) != 0:
            item = self.items.pop(0)
        self.lock.release()
        return item

    def empty(self):
        self.lock.aquire()
        is_empty = (len(self.items) == 0)
        self.lock.release()
        return is_empty

    def top(self):
        item = None
        self.lock.aquire()
        if len(self.items) != 0:
            item = self.items[0]
        self.lock.release()
        return item
