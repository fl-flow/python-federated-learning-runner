from uuid import uuid4
from pathlib import Path
from datetime import datetime
from ...abstract import AbstractAddress


class Address(AbstractAddress):
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / 'var'/ 'storage'
    def __init__(self, path=None, **kw):
        self.path = path or str(self.ROOT_DIR / str(datetime.now().date()) / uuid4().hex)
        self.args = {
            'path': self.path
        }
        super().__init__()
