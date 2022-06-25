from pickle import dumps, loads


class AbstractAddress():
    pass


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
