class Meta():
    def __init__(self, features: tuple, label: bool, ID: bool=True):
        self._id = ID
        self._label = label
        assert isinstance(features, tuple), 'error features'
        for i in features:
            assert isinstance(i, str), 'error feature name'
        self._features = features

    def id(self):
        return self._id

    def label(self):
        return self._label

    def features(self):
        return self._features


class DataFrame():
    def __init__(
        self,
        features: tuple,
        label: bool,
        ID: bool=True,
    ):
        self._meta = Meta(
            features=features,
            label=label,
            ID=ID,
        )


    # meta info start
    def id(self):
        return self._meta.id

    def label(self):
        return self._meta.label

    def features(self):
        return self._meta.features
    # meta info end


    @classmethod
    def load_data_from_storage(cls, id_address, data_address, label_address):
        pass

    @classmethod
    def load_data_from_iter(cls, id_iteration, data_iteration, label_iteration):
        pass

    @property
    def feature(self):
        '''
            tensor 对应的 特征矩阵
        '''

    @property
    def label(self):
        '''
            tensor 对应的 标签向量
        '''

    @property
    def id(self):
        '''
            tensor 对应的 id向量
        '''
