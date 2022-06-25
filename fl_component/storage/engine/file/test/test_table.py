import unittest
from fl_component.storage.engine.file.table import Table


class SessionTest(unittest.TestCase):
    def test_put(self):
        data = [(1, 2), ('a', 2)]
        table = Table()
        table.put_all(data)
        table.f.seek(0)
        assert list((table)) == data
