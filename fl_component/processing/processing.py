from uuid import uuid4
from pickle import dumps
from base64 import b64encode
from collections.abc import Iterable
from functools import cached_property

FIFO_W_PATH = '/Users/xinchengshao/Desktop/workspace/dag-scheduler/process_pipe.ipc'
FIFO_R_PATH = '/Users/xinchengshao/Desktop/workspace/dag-scheduler/process_pipe_w.ipc'



class Process():
    def __init__(
        self,
        cmd,
        memory,
        data,
        stream=False
    ):
        assert isinstance(cmd, str), 'error cmd'
        assert isinstance(memory, int), 'error memory'
        self.cmd = cmd
        self.memory = memory
        self.data = data
        self.stream = stream
        if stream:
            assert isinstance(data, Iterable), 'data required iterable on mode stream'
        self.split = f'-------------------{uuid4().hex}'

    @cached_property
    def w(self):
        return open(FIFO_W_PATH, 'w')

    @cached_property
    def r(self):
        return open(FIFO_R_PATH, 'r')

    def encode(self, v):
        return b64encode(str(v).encode()).decode()

    # TODO: semaphore
    def run(self):
        self.w.write(
            f'{self.encode(self.cmd)},{self.encode(self.memory)}\n'
        )
        self.w.flush()
        d = self.r.readline()
        print(d)
        self.__write_data()

    def __write_data_obj(self):
        split_ = self.split + '\n'
        self.w.write(
            f'{len(split_)}\n'
        )
        self.w.write(split_)
        d = self.encode(dumps(self.data))
        self.w.write(
            f'{len(d)}\n'
        )
        self.w.write(d + '\n')
        self.w.flush()
        self.__read_data()

    def __write_data(self):
        if self.stream:
            # TODO:
            return
        self.__write_data_obj()

    def __read_data(self):
        while 1:
            count = self.r.readline().strip()
            if not count:
                break
            d = self.r.read(int(count))
            print(d)