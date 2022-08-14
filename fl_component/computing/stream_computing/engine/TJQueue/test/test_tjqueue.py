import unittest
from fl_component.computing.stream_computing.engine.TJQueue.session import Session


class ArgumentParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ds = Session.parallelize([1, 2, 3])

    def test_iter(self):
        assert list(self.ds.collect_without_key()) == [1, 2, 3], 'error iter'

    def test_map(self):
        assert list(
            self.ds.map(
                lambda key, v: (key, v + 1)
            ).collect_without_key()
        ) == [2, 3, 4], 'error map'