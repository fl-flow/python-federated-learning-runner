import typing
from json import loads

from exception.executer.parser import DataModelParserError


class BaseInputType():
    def __init__(self, source: typing.List[str], annotation):
        if not source:
            raise DataModelParserError(msg=f'input.type.source is required')
        if not isinstance(source, list):
            raise DataModelParserError(msg=f'input.type.source require list')
        try:
            annotation = int(annotation)
        except ValueError:
            raise DataModelParserError(msg=f'input.model.type annotation require int')
        if annotation >= len(source):
            raise DataModelParserError(msg=f'input.model.type annotation should less than source.length')
        self.source = source
        self.annotation = annotation



class Data(BaseInputType):
    pass


class Model(BaseInputType):
    pass


class Input():
    ALLOWED_TYPES_MAP = {'model': Model, 'data': Data}
    def __init__(self, raw_list):
        self._raw_list = raw_list
        for i in self.ALLOWED_TYPES_MAP: setattr(self, i, [])
        for _raw_dict, annotation in raw_list:
            raw_dict = loads(_raw_dict)
            _type = raw_dict.get('type', 'data')
            cls = self.ALLOWED_TYPES_MAP.get(_type)
            if not cls:
                raise DataModelParserError(msg=f'error type {_type}')
            getattr(self, _type).append(
                cls(
                    source=raw_dict.get('value'),
                    annotation=annotation
                )
            )
