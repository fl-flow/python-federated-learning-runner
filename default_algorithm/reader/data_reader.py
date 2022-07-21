from utils.protocol_path_parser import parse
from fl_component.storage.finder import Finder
from fl_component.storage.register import Register as StorageRegister
from fl_component.algorithm import BaseAlgorithm, BaseAlgorithmParameter
from fl_component.computing.stream_computing.register import Register as ComputingRegister


class Parameter(BaseAlgorithmParameter):
    urls = None


class Reader(BaseAlgorithm):
    parameter = Parameter()

    def __init__(self):
        self.urls = None

    def run(self):
        self.validate()
        computing_session = ComputingRegister.get_engine()
        self.output_data = [
            computing_session.parallelize(
                data=Finder.load(url),
                include_key=False,
            )
            for url in self.urls
        ]

    def validate(self):
        urls = self.parameter.urls
        if not isinstance(urls, list):
            urls = [urls]
        for url in urls:
            if not isinstance(url, str):
                raise self.Error(msg='url is required for reader')
            ret = parse(url)
            if not ret:
                raise self.Error(msg=f'error url {url}')
        self.urls = urls
