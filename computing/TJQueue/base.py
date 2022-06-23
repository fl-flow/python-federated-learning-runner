from pickle import loads, dumps
from TJQueue.queue import Queue as TJ_Queue


class Queue(TJ_Queue):
    def push(self, msg):
        super().push(dumps(msg))

    def pop(self):
        return loads(super().pop())
