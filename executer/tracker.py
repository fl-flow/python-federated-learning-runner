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
            if i.source
        ]

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
