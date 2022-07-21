import numpy as np
from conf.conf import TENSOR_ENGINE


class Meta():
    def __init__(self, features: tuple, label: bool, ID: bool=True):
        self._id = ID
        self._label = label
        assert isinstance(features, (tuple, list)), 'error features'
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
        feature_names: tuple,
        has_label: bool,
        has_id: bool=True,
    ):
        self._meta = Meta(
            features=feature_names,
            label=has_label,
            ID=has_id,
        )


    # meta info start
    def has_id(self):
        return self._meta.id

    def has_label(self):
        return self._meta.label

    def feature_names(self):
        return self._meta.features
    # meta info end


    def load_data_from_storage(self, id_storage, feature_storage, label_storage):
        if TENSOR_ENGINE == 'numpy':
            self.id = np.array(list(id_storage))
            self.label = np.array(list(label_storage))
            self.feature = np.array(list(feature_storage))
        else:
            raise
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
