from ..abstract import AbstractSession, AbstractDataSet


class Session(AbstractSession):
    def __init__(
        self,
        session_id: str,
        **kw: dict
    ):
        pass


    def load(
        self,
        address, # TODO:
        partitions: int
    ):
        raise NotImplementedError()


class DataSet(AbstractDataSet):
    pass