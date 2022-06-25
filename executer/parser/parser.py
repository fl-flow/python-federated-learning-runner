import typing
from json import loads, dumps


class Input():
    def __init__(self, raw_dict):
        self._raw_dict = raw_dict
        self.__set(key='m', attr='M')
        self.__set(key='d', attr='D')

    def __set(self, key, attr):
        v = self._raw_dict.get(key, [])
        assert isinstance(v ,list), f'error input.{key}'
        setattr(self, attr, v)


class Output():
    def __init__(self):
        self.M = []
        self.D = []

    def build_output(self):
        assert (self.M, list), 'error Output.M'
        assert (self.D, list), 'error Output.D'
        return {
            'm': self.M,
            'd': self.D,
        }


class Parser():
    def deserialize_input_data(
        self,
        raw_inputs: typing.List[str]
    ) -> typing.List[Input]:
        return [
            Input(loads(i))
            for i in raw_inputs
        ]

    def serialize_output_data(
        self,
        outputs: typing.List[Output]
    ) -> typing.List[str]:
        return [
            dumps(i.build_output())
            for i in outputs
        ]

    def parse_parameter(self, raw_parameters):
        return loads(raw_parameters)

    def parse_common_parameter(self, raw_common_parameter):
        return loads(raw_common_parameter)
