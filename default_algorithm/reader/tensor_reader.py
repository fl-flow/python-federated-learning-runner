from utils.protocol_path_parser import parse
from fl_component.storage.finder import Finder
from fl_component.computing.tensor_computing import DataFrame
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
        self.output_tensor = [
            DataFrame(
                feature_names=meta_['feature_names'],
                has_label=meta_['has_label'],
                has_id=meta_['has_id'],
            ).load_data_from_storage(
                id_storage=Finder.load(meta_['id_address']),
                feature_storage=Finder.load(meta_['feature_address']),
                label_storage=Finder.load(meta_['label_address'])
            )
        ]

    def validate(self):
        if self.parameter.url == None:
            raise self.Error(msg=f'{i} is required for tensor reader')
        ret = parse(self.parameter.url)
        if not ret:
            raise self.Error(msg=f'error url {self.parameter.url}')
