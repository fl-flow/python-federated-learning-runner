import unittest
from fl_component.algorithm.argument_parser import ArgumentParser


class ArgumentParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        class arg():
            a = 'z'

        class argb():
            a = arg()
            b = 2

        self.parameter = argb()

    def test_parse(self):
        ap = ArgumentParser(
            parameter_cls=self.parameter,
            parameter={
                'a': {
                    'a': 't'
                },
                'b': 3
            }
        )
        ap.parse()
        assert self.parameter.a.a == 't'
        assert self.parameter.b == 3
