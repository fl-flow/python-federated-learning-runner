import mars.tensor as mt


class Meta():
    def __init__(self, features: tuple, label: bool, ID: bool=True):
        self._id = ID
        self._label = label
        assert isinstance(features, (tuple, list)), 'error features'
        for i in features:
            assert isinstance(i, str), 'error feature name'
        self._features = features

    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def features(self):
        return self._features


class DataFrame():
    def __init__(
        self,
        feature_names: tuple,
    ):
        self._meta = Meta(
            features=feature_names,
            label=False,
            ID=False,
        )


    def re_feature_names(self, feature_names):
        self._meta._features = feature_names

    # meta info start
    @property
    def has_id(self):
        return self._meta.id

    @property
    def has_label(self):
        return self._meta.label

    @property
    def feature_names(self):
        return self._meta.features
    # meta info end


    def load_data_from_storage(self, id_storage, feature_storage, label_storage):
        _id_list = list(id_storage)
        _label_list = list(label_storage)
        self._meta._id = True if _id_list else False
        self._meta._label = True if _label_list else False
        self.id = mt.tensor(_id_list)
        self.label = mt.tensor(_label_list)
        self.feature = mt.tensor(list(feature_storage))
        return self

    # def load_data_from_iter(cls, id_iteration, data_iteration, label_iteration):
    #     pass

    @property
    def feature(self):
        '''
            tensor 对应的 特征矩阵
        '''
        return self._feature

    @feature.setter
    def feature(self, v):
        self._feature = v

    @property
    def label(self):
        '''
            tensor 对应的 标签向量
        '''
        return self._label

    @label.setter
    def label(self, v):
        self._label = v

    @property
    def id(self):
        '''
            tensor 对应的 id向量
        '''
        return self._id

    @id.setter
    def id(self, v):
        '''
            tensor 对应的 id向量
        '''
        self._id = v
