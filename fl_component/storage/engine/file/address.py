from uuid import uuid4
from pathlib import Path
from ..abstract import AbstractAddress


class Address(AbstractAddress):
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent / 'var'/ 'storage'
    def __init__(self, uid, path=None):
        self.path = path or str(self.ROOT_DIR / uuid4())
