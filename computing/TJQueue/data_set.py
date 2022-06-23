from uuid import uuid4
from .base import Queue
from TJQueue.fifo_io.reader import EOFError


class DataSet():
    def __init__(self, queue: Queue):
        self.queue = queue

    def map(self, func):
        new_queue = Queue(name=uuid4().hex)
        while 1:
            try:
                new_queue.push(func(*self.queue.pop()))
            except EOFError:
                break

    def collect(self):
        while 1:
            try:
                yield self.queue.pop()
            except EOFError:
                break

    def __iter__(self):
        return self.collect()
