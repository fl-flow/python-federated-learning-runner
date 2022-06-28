from utils.importer import import_class
from conf.conf import STORAGE_ENGINE_MAP
from utils.protocol_path_parser import parse as parse_path
from exception.fl_component.storage import (
    StorageEngineError,
    StorageSourceParseError,
)


class Finder():
    @classmethod
    def load(self, source: str):
        ret = parse_path(source)
        if not ret:
            raise StorageSourceParseError(
                msg=f'source {source} parse error'
            )
        engine, args = ret
        engine_conf = STORAGE_ENGINE_MAP.get(engine)
        if not engine_conf:
            raise StorageEngineError(
                msg=f'storage engine {engine} is invalid'
            )
        address_cls = import_class(engine_conf['module']['address'])
        table_cls = import_class(engine_conf['module']['table'])
        return table_cls(
            address_cls(**args)
        )
