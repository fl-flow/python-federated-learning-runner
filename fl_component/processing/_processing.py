from pickle import loads
from base64 import b64decode
from functools import cached_property

from .output import Output


OUTPUT_INSTANCE = None


def get_output_instance():
    assert OUTPUT_INSTANCE, 'error'
    return OUTPUT_INSTANCE


class ConsumeStreamError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class _process():
    def __init__(self):
        self.split_item = None
        self.split_type = None
        self.target = None
        self.args = None
        self.stream_current_index = 0
        self.output = None
        self.parse()

    def parse(self):
        self.split_item = input()
        self.split_type = input()
        self.target = self.objs[0]
        self.args = self.objs[1:]
        self.stream_length = self.parse_item(input())
        self.stream = [StreamArg(i, self) for i in range(self.stream_length)]
        self.output = Output(self.split_item)
        global OUTPUT_INSTANCE
        OUTPUT_INSTANCE = self.output

    def run(self):
        # TODO: stream output
        ret = self.target(*(self.args + self.stream))
        self.output.output_ret(ret)

    @cached_property
    def objs(self):
        _objs = []
        while 1:
            i = input()
            if i == self.split_item:
                continue
            if i == self.split_type:
                break
            _objs.append(self.parse_item(i))
        return _objs

    def parse_item(self, i):
        return loads(b64decode(i.encode()))

    def consume_stream(self, index):
        if self.stream_current_index > index:
            raise ConsumeStreamError(msg='stream can only consume once')
        if self.stream_current_index != index:
            raise ConsumeStreamError(
                msg=f'consume stream error, must consume item {self.stream_current_index} before {index}'
            )
        while 1:
            i = input()
            if i == self.split_item:
                self.stream_current_index += 1
                break
            yield self.parse_item(i)


class StreamArg():
    def __init__(self, index: int, process: _process):
        self.index = index
        self.process = process

    def __iter__(self):
        yield from self.process.consume_stream(self.index)
