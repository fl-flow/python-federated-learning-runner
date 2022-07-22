from utils.protocol_path_parser import parse
from fl_component.storage.finder import Finder
from fl_component.algorithm import BaseAlgorithm, BaseAlgorithmParameter


class Parameter(BaseAlgorithmParameter):
    url = None


class Reader(BaseAlgorithm):
    parameter = Parameter()

    def __init__(self):
        self.urls = None

    def run(self):
        self.validate()
        meta_ = list(Finder.load(self.parameter.url))[0]
        self.output_tensor_ret = [
            {
                'id': meta_['id_address'],
                'label': meta_['label_address'],
                'feature': meta_['feature_address'],
                'meta': self.parameter.url
            }
        ]

    def validate(self):
        if self.parameter.url == None:
            raise self.Error(msg=f'{i} is required for tensor reader')
        ret = parse(self.parameter.url)
        if not ret:
            raise self.Error(msg=f'error url {self.parameter.url}')
