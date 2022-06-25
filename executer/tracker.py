from base64 import b64decode

from .parser.parser import Parser
from utils.logger import Logger


logger = Logger(__file__)


class Tracker():
    def __init__(self, parser=None):
        self.parser = parser or Parser()
        self.common_parameter = None
        self.parameters = None
        self.input_length = 0
        self.out_length = 0
        self.get_input()

    def get_input(self):
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
        self.get_input_data()

    def get_input_data(self) -> list:
        self.input = self.parser.deserialize_input_data([
            (b64decode(input())).decode('utf-8')
            for i in range(self.input_length)
        ])
        logger.info(f'got input: {[i._raw_dict for i in self.input]}')
