import os
from functools import cached_property

from .address import Address
from ...abstract import AbstractTable


class Table(AbstractTable):
    def __init__(self, address: Address=None):
        self.address = address or Address()
        path = self.address.path

        # hash path
        dirs, file_path = os.path.split(path)
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        self.f = open(path, 'wb+')

    def collect(self):
        while 1:
            d = self.f.readline()
            if d == b'':
                break
            yield self.loads(d.strip())

    def put_all(self, data_list):
        for i in data_list:
            self.f.write(self.dumps(i))
            self.f.write(b'\n')
