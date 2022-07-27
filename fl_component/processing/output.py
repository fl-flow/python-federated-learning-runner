import sys
from pickle import dumps
from base64 import b64encode


class Output():
    STREAM = 'stream'
    OBJ = 'object'
    def __init__(self, split):
        self.split = split
        self.used = False

    def output(self, item, stream=False):
        self.used = True
        # TODO: stream
        if not stream:
            self._output_obj(item)
            return
        self._output_stream(item)

    def _output_obj(self, item):
        sys.stdout.write(self.OBJ + '\n')
        sys.stdout.write(b64encode(dumps(item)).decode() + '\n')
        sys.stdout.write(self.split + '\n')

    def _output_stream(self, item):
        sys.stdout.write(self.STREAM + '\n')
        for i in item:
            sys.stdout.write(b64encode(dumps(i)).decode() + '\n')
        sys.stdout.write(self.split + '\n')

    def output_ret(self, ret):
        if self.used:
            return
        if not isinstance(ret, (list, tuple, set)):
            self.output(ret)
            return
        for i in ret:
            self.output(i)
