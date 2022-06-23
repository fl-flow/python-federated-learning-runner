from functools import cached_property

from .address import Address
from ..abstract import AbstractTable


class Table(AbstractTable):
    def __init__(self, address:Address):
        self.f = open(address, 'ab+')

    def collect(self):
        pass
