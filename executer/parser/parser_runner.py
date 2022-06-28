from base64 import b64decode

from .parser import Parser
from utils.logger import Logger


logger = Logger(__file__)


class ParserRunner():
    def __init__(self, parser=None):
        self.parser = parser or Parser()
        self.task_info = None
        self.common_parameter = None
        self.parameters = None
        self.input_length = 0
        self.out_length = 0

    def load(self):
        self.load_conf()

    def load_conf(self):
        self.task_info = self.parser.parse_task_info(
            (b64decode(input())).decode('utf-8')
        )
        self.common_parameter = self.parser.parse_common_parameter(
            (b64decode(input())).decode('utf-8')
        )
        logger.info(f'got common_parameter: {self.common_parameter}')
        self.parameters = self.parser.parse_parameter(
            (b64decode(input())).decode('utf-8')
        )
        logger.info(f'got parameters: {self.parameters}')
        self.input_length = int((b64decode(input())).decode('utf-8'))
        logger.info(f'got input_length: {self.input_length}')
        self.out_length = int((b64decode(input())).decode('utf-8'))
        logger.info(f'got out_length: {self.out_length}')
        self.load_input_data()

    def load_input_data(self) -> list:
        self.input = self.parser.deserialize_input_data([
            (
                (b64decode(input())).decode('utf-8'),
                (b64decode(input())).decode('utf-8')
            )
            for i in range(self.input_length)
        ])
        logger.info(f'got input data: {[i.source for i in self.input.data]}')
        logger.info(f'got input model: {[i.source for i in self.input.model]}')
