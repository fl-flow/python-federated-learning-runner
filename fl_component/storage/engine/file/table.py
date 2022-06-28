import os
from functools import cached_property

from .address import Address
from ...abstract import AbstractTable
from exception.fl_component.storage import StorageSourceParseError


class Table(AbstractTable):
    def __init__(self, address: Address=None):
        self.address = address or Address()

        # hash path
        dirs, file_path = os.path.split(self.address.path)
        if not os.path.exists(dirs):
            os.makedirs(dirs)

    @cached_property
    def wf(self):
        return open(self.address.path, 'ab+')

    @cached_property
    def rf(self):
        try:
            return open(self.address.path, 'rb')
        except FileNotFoundError:
            raise StorageSourceParseError(
                msg=f'{self.address.path} FileNotFound'
            )
    def collect(self):
        self.rf.seek(0)
        while 1:
            d = self.rf.readline()
            if d == b'':
                break
            yield self.loads(d.strip())

    def put_all(self, data_list):
        for i in data_list:
            self.wf.write(self.dumps(i))
            self.wf.write(b'\n')
        self.wf.flush()
