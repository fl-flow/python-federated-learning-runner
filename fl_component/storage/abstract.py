from pickle import dumps, loads


class AbstractAddress():
    ARGS_KEYS = ('username', 'password', 'path', 'query', 'host', 'port')
    def __init__(self, *args, **kw):
        assert hasattr(self, 'args'), 'error self.args is required'
        assert all([(i in self.ARGS_KEYS) for i in self.args])


class AbstractTable():
    def collect(self):
        raise NotImplementedError()

    def __iter__(self):
        return self.collect()

    # TODO: 更换跨语言 序列化 方案
    def dumps(self, data):
        return dumps(data)

    def loads(self, data):
        return loads(data)
