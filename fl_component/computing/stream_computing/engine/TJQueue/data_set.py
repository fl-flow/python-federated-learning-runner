from uuid import uuid4
from .utils import encode, decode
from TJQueue.queue import get_queue
from TJQueue.exception import EOFError
from ..abstract import AbstractDataSet


class DataSet(AbstractDataSet):
    def __init__(self, queue):
        self._queue = queue

    def __iter__(self):
        self._queue.reset_reader()
        return self

    def __next__(self):
        try:
            return decode(self._queue.pop())
        except EOFError:
            raise StopIteration()

    def collect_without_key(self):
        for i in self:
            yield i[1]

    def map(self, func):
        q =  get_queue(uuid4().hex)
        for i in self:
            q.push(encode(func(*i)))
        q.end()
        return DataSet(q)