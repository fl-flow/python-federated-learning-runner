from json import loads

from exception.executer.parser import DataModelParserError


class Data():
    def __init__(self, storage_source: str):
        if not storage_source:
            raise DataModelParserError(msg=f'input.data.source is required')
        self.source = storage_source


class Model():
    def __init__(self, storage_source: str):
        if not storage_source:
            raise DataModelParserError(msg=f'input.model.source is required')
        self.source = storage_source


class Input():
    ALLOWED_TYPES_MAP = {'model': Model, 'data': Data}
    def __init__(self, raw_list):
        self._raw_list = raw_list
        for i in self.ALLOWED_TYPES_MAP: setattr(self, i, [])
        for _raw_dict in raw_list:
            raw_dict = loads(_raw_dict)
            _type = raw_dict.get('type', 'data')
            cls = self.ALLOWED_TYPES_MAP.get(_type)
            if not cls:
                raise DataModelParserError(msg=f'error type {_type}')
            getattr(self, _type).append(cls(raw_dict.get('value')))
