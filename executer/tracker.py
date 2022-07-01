import sys
from json import dumps
from base64 import b64encode
from functools import cached_property

from utils.logger import Logger
from fl_component.storage.finder import Finder
from .parser.parser_runner import ParserRunner
from fl_component.storage.register import Register as StorageRegister
from fl_component.computing.register import Register as ComputingRegister


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
        ]

    @cached_property
    def input_model(self):
        # TODO:
        return self.parser_runner.input.model

    def __save_output_data(self, output_data):
        # TODO: save
        engine, table_engin, address_engine = StorageRegister.get_engine()
        for i in output_data:
            address = address_engine()
            table_engin(address).put_all(i)
            args = address.args
            ARGS_KEYS = ('username', 'password', 'path', 'query', 'host', 'port')
            yield f"{engine}://{args.get('username', '')}@{args.get('passwd', '')}:{args.get('port', '')}{args.get('path', '')}?{'&'.join([k+'='+v for k, v in args.get('query', {}).items()])}"

    def save_output_data(self, output_data):
        logger.info(f'got output_data: {output_data}')
        output_data = list(self.__save_output_data(output_data))
        sys.stdout.write(b64encode(dumps({
            'type': 'data',
            'value': output_data,
        }).encode()).decode() + '\n')
        return output_data


    def save_output_model(self, output_model):
        # TODO:
        sys.stdout.write(b64encode(dumps({
            'type': 'model',
            'value': output_model,
        }).encode()).decode() + '\n')
