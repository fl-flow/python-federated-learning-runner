import sys
from json import dumps
from base64 import b64encode
from functools import cached_property

from utils.logger import Logger
from fl_component.storage.finder import Finder
from .parser.parser_runner import ParserRunner
from fl_component.computing.tensor_computing import DataFrame
from fl_component.storage.register import Register as StorageRegister
from fl_component.computing.stream_computing.register import Register as ComputingRegister


logger = Logger(__file__)


class Tracker():
    def __init__(self, parser_runner: ParserRunner):
        self.parser_runner = parser_runner

    @cached_property
    def input_data(self):
        computing_session = ComputingRegister.get_engine()
        return [
            computing_session.parallelize(
                data=Finder.load(i.source),
                include_key=False,
            )
            for i in self.parser_runner.input.data
            if i.source
        ]

    @cached_property
    def input_tensor(self):
        tensors = []
        for i in self.parser_runner.input.tensor:
            if not i.source:
                continue
            meta_ = list(Finder.load(i.source['meta']))[0]
            tensors.append(
                DataFrame(
                    feature_names=meta_['feature_names'],
                    has_label=meta_['has_label'],
                    has_id=meta_['has_id'],
                ).load_data_from_storage(
                    id_storage=Finder.load(i.source['id']),
                    feature_storage=Finder.load(i.source['feature']),
                    label_storage=Finder.load(i.source['label'])
                )
            )
        return tensors

    @cached_property
    def input_model(self):
        return [
            list(Finder.load(i.source))[0]
            for i in self.parser_runner.input.model
            if i.source
        ]

    def __save(self, output_data):
        # TODO: save
        engine, table_engin, address_engine = StorageRegister.get_engine()
        for i in output_data:
            yield table_engin(address_engine()).save(i)
            # address = address_engine()
            # table_engin(address).put_all(i)
            # args = address.args
            # yield f"{engine}://{args.get('username', '')}@{args.get('passwd', '')}:{args.get('port', '')}{args.get('path', '')}?{'&'.join([k+'='+v for k, v in args.get('query', {}).items()])}"

    def save_output_data(self, output_data):
        logger.info(f'got output_data: {output_data}')
        output_data = list(self.__save(output_data))
        sys.stdout.write(b64encode(dumps({
            'type': 'data',
            'value': output_data,
        }).encode()).decode() + '\n')
        return output_data


    def save_output_model(self, output_model):
        logger.info(f'got output_model: {output_model}')
        output_model = list(self.__save(output_model))
        sys.stdout.write(b64encode(dumps({
            'type': 'model',
            'value': output_model,
        }).encode()).decode() + '\n')
        return output_model

    def save_output_tensor(self, output_tensor):
        logger.info(f'got output_tensor: {output_tensor}')
        engine, table_engin, address_engine = StorageRegister.get_engine()
        sys.stdout.write(b64encode(dumps({
            'type': 'tensor',
            'value': [
                {
                    'id': table_engin(address_engine()).save(t.id),
                    'label': table_engin(address_engine()).save(t.label) if t.has_label else None,
                    'feature': table_engin(address_engine()).save(t.feature),
                    'meta': table_engin(address_engine()).save([{
                        'has_id': True,
                        'has_label': t.has_label,
                        'feature_names': t.feature_names
                    }])
                }
                for t in output_tensor
            ],
        }).encode()).decode() + '\n')
        return []

    def save_summary(self, summary):
        logger.info(f'got summary: {summary}')
        sys.stdout.write(b64encode(dumps(summary).encode()).decode() + '\n')
        return summary
