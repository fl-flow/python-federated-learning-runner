from base64 import b64decode


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
        self.parameters = self.parse_parameter(
            (b64decode(input())).decode('utf-8')
        )
        self.input_length = int((b64decode(input())).decode('utf-8'))
        self.out_length = int((b64decode(input())).decode('utf-8'))
        self.get_input_data()

    def get_input_data(self) -> list:
        self.input = self.parser.deserialize_input_data([
            (b64decode(input())).decode('utf-8')
            for i in range(self.input_length)
        ])
