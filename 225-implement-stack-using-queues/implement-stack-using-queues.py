class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        self._queue.appendleft(x)

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return len(self._queue) == 0