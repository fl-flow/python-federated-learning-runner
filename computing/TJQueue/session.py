from uuid import uuid4

from .base import Queue
from ..abstract import AbstractSession
from .data_set import DataSet


class Session(AbstractSession):
    @classmethod
    def parallelize(
        self,
        data,
        partition: int,
        include_key: bool,
    ) -> DataSet:
        q = Queue(uuid4().hex)
        for k, v in (data if include_key else enumerate(data)): q.push((k, v))
        q.end()
        q.flush()
        return DataSet(queue=q)
