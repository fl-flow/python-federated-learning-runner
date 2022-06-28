import typing
from utils.importer import import_class
from conf.conf import COMPUTING_ENGINE_MAP


class Register():
    ENGINE = None

    @classmethod
    def register_engine(
        cls,
        session_id: str,
        engine: str,
    ):
        assert cls.ENGINE == None, 'duplicate register'
        assert engine in COMPUTING_ENGINE_MAP, f'error engine {engine}'
        module = COMPUTING_ENGINE_MAP[engine]['module']
        cls.ENGINE = import_class(module)

    @classmethod
    def get_engine(cls):
        assert cls.ENGINE != None, 'register_engine before get_engine'
        return cls.ENGINE
