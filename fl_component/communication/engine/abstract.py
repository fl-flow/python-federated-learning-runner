import types


class AbstractEngine():
    def pull(self, data, parties, tag: str):
        raise NotImplementedError()

    def push(self, data, parties, tag: str):
        raise NotImplementedError()
