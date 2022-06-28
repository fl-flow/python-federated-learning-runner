import typing
from utils.importer import import_class
from conf.conf import STORAGE_ENGINE_MAP


class Register():
    TABLE_ENGIN = None
    ADDRESS_ENGINE = None
    ENGINE = None

    @classmethod
    def register_engine(
        cls,
        session_id: str,
        engine: str,
    ):
        assert cls.ENGINE == None, 'duplicate register'
        assert engine in STORAGE_ENGINE_MAP, f'error engine {engine}'
        cls.ENGINE = engine
        module = STORAGE_ENGINE_MAP[engine]['module']
        table_module = module['table']
        address_module = module['address']
        cls.TABLE_ENGIN = import_class(table_module)
        cls.ADDRESS_ENGINE = import_class(address_module)

    @classmethod
    def get_engine(cls):
        assert cls.ENGINE != None, 'register_engine before get_engine'
        return cls.ENGINE, cls.TABLE_ENGIN, cls.ADDRESS_ENGINE
