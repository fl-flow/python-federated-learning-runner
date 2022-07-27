from uuid import uuid4
from pickle import dumps, loads
from collections.abc import Iterable
from functools import cached_property
from base64 import b64encode, b64decode

from .output import Output

FIFO_W_PATH = '/Users/xinchengshao/Desktop/workspace/dag-scheduler/process_pipe.ipc'
FIFO_R_PATH = '/Users/xinchengshao/Desktop/workspace/dag-scheduler/process_pipe_w.ipc'



class Popen():
    def __init__(
        self,
        cmd,
        memory,
        obj: list=None,
        stream: list=None,
    ):
        obj = obj or []
        stream = stream or []
        assert isinstance(cmd, str), 'error cmd'
        assert isinstance(memory, int), 'error memory'
        assert isinstance(obj, list), 'error obj'
        assert all([isinstance(i, Iterable) for i in stream]), 'error stream'
        self.cmd = cmd
        self.memory = memory
        self.obj = obj
        self.stream = stream
        self.split_item = f'-----------------item-{uuid4().hex}'
        self.split_type = f'----------------obj-stream-{uuid4().hex}'

    @cached_property
    def w(self):
        return open(FIFO_W_PATH, 'w')

    @cached_property
    def r(self):
        return open(FIFO_R_PATH, 'r')

    def encode(self, v):
        return b64encode(v).decode()

    # TODO: semaphore
    def run(self):
        self.w.write(
            f'{self.encode(self.cmd.encode())},{self.encode(str(self.memory).encode())}\n'
        )
        self.w.flush()
        d = self.r.readline()
        self.__write_data()
        return self.__read_data()

    def __write_split_item(self):
        split_ = self.split_item + '\n'
        self.w.write(f'{len(split_)}\n{split_}')

    def __write_split_type(self):
        split_ = self.split_type + '\n'
        self.w.write(f'{len(split_)}\n{split_}')

    def __write_done(self):
        self.w.write('\n')

    def __write_item(self, i):
        d = self.encode(dumps(i)) + '\n'
        self.w.write(
            f'{len(d)}\n{d}'
        )

    def __write_data(self):
        self.__write_split_item()
        self.__write_split_type()
        obj_length = len(self.obj)
        if obj_length:
            for i in self.obj[:-1]:
                self.__write_item(i)
                self.__write_split_item()
            self.__write_item(self.obj[-1])
        self.__write_split_type()
        self.__write_item(len(self.stream))
        for i in self.stream:
            for ii in i:
                self.__write_item(ii)
            self.__write_split_item()
        self.__write_done()
        self.w.flush()

    def __read_data(self):
        g = self.__read_chunk_data_line()
        self._flag = True
        while 1:
            assert self._flag, 'consume error'
            try:
                type_ = next(g)
            except StopIteration:
                break
            if type_ == Output.STREAM: # TODO:
                self._flag = False
                yield StreamRet(self.__stream(g))
            elif type_ == Output.OBJ:
                ds = list(self.__stream(g))
                assert len(ds) == 1, 'error'
                yield ds[0]
            else:
                raise

    def __stream(self, g):
        for i in g:
            if i == self.split_item:
                self._flag = True
                break
            yield loads(b64decode(i.encode()))

    def __read_chunk_data_line(self):
        buf = ''
        while 1:
            count = self.r.readline().strip()
            if not count:
                break
            d = self.r.read(int(count))
            if not d:
                break
            buf += d
            bufs = buf.split('\n')
            if len(bufs) > 1:
                for i in bufs[:-1]:
                    yield i
                buf = bufs[-1]


class StreamRet():
    def __init__(self, gen):
        self.gen = gen
        self.done = False

    def __iter__(self):
        assert not self.done, 'err stream can only consume once'
        self.done = True
        return self.gen
