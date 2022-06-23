import unittest
from computing.TJQueue.session import Session


class SessionTest(unittest.TestCase):
    def test_parallelize(self):
        d = [1, 5, 6]
        ds = Session.parallelize(
            data=d,
            partition=2,
            include_key=False
        )
        print(ds, 1111)
