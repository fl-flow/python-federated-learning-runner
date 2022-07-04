from pickle import dumps, loads


class AbstractAddress():
    ARGS_KEYS = ('username', 'password', 'path', 'query', 'host', 'port')
    def __init__(self, *args, **kw):
        assert hasattr(self, 'args'), 'error self.args is required'
        assert all([(i in self.ARGS_KEYS) for i in self.args])


class AbstractTable():
    def __init__(self, address: AbstractAddress=None):
        raise NotImplementedError()

    def collect(self):
        raise NotImplementedError()

    def __iter__(self):
        return self.collect()

    # TODO: 更换跨语言 序列化 方案
    def dumps(self, data):
        return dumps(data)

    def loads(self, data):
        return loads(data)

    def save(self, data_list):
        self.put_all(data_list)
        args = self.address.args
        return f"{self.engine}://{args.get('username', '')}@{args.get('passwd', '')}:{args.get('port', '')}{args.get('path', '')}?{'&'.join([k+'='+v for k, v in args.get('query', {}).items()])}"

    def put_all(self, data_list):
        raise NotImplementedError()

    @property
    def engine(self):
        raise NotImplementedError()
