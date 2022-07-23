class FLInput():
    __slots__ = ['data', 'model', 'tensor', 'role']
    def __init__(self, **kw):
        for k, v in kw.items():
            if k in self.__slots__:
                setattr(self, k, v)


class FLOutput():
    __slots__ = [
        'data',
        'model',
        'tensor',
        'summary',
        'data_ret',
        'model_ret',
        'tensor_ret',
    ]
    def __init__(self, **kw):
        self.data = []
        self.model = []
        self.tensor = []

        self.summary = {}

        self.data_ret = None
        self.model_ret = None
        self.tensor_ret = None
