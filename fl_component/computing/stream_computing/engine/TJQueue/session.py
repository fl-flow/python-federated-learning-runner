from uuid import uuid4

from .utils import encode
from .data_set import DataSet
from TJQueue.queue import get_queue
from fl_component.storage.finder import Finder
from ..abstract import AbstractSession


class Session(AbstractSession):
    @classmethod
    def load(
        cls,
        address, # TODO:
        partitions: int,
        include_key=False
    ):
        return cls.parallelize(
            data=Finder.load(address),
            include_key=include_key,
        )

    @classmethod
    def parallelize(
        cls,
        data,
        include_key=False,
    ):
        q =  get_queue(uuid4().hex)
        for i in (data if include_key else enumerate(data)):
            q.push(encode(i))
        q.end()
        return DataSet(q)