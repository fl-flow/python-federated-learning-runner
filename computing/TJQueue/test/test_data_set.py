import unittest
from computing.TJQueue.session import Session


class DataTestTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.raw_d = [('a', 1), ('z', 5), (7, 6)]
        self.data_set = Session.parallelize(
            data=self.raw_d,
            partition=2,
            include_key=True
        )

    def test_iter(self):
        assert(list(self.data_set) == self.raw_d)
