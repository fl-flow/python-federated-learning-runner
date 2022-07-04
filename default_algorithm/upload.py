from utils.protocol_path_parser import parse
from fl_component.storage.register import Register as StorageRegister
from fl_component.algorithm import BaseAlgorithm, BaseAlgorithmParameter


class Parameter(BaseAlgorithmParameter):
    url = None


def readline(f):
    while 1:
        line = f.readline()
        if line == '':
            break
        yield line.strip().split(',')

        
class Upload(BaseAlgorithm):
    parameter = Parameter()
    SchemaMethodMap = {
        'file': 'file_schema'
    }

    def __init__(self):
        self.schema = None
        self.components = None

    def run(self):
        self.validate()
        getattr(self, self.SchemaMethodMap[self.schema])(self.components)

    def validate(self):
        url = self.parameter.url
        if not isinstance(url, str):
            raise self.Error(msg='url is required for upload')
        ret = parse(url)
        if not ret:
            raise self.Error(msg=f'error url {url}')
        schema, components = ret
        method_name = self.SchemaMethodMap.get(schema)
        if not method_name:
            raise self.Error(msg=f'error schema {url}')
        self.schema = schema
        self.components = components

    def file_schema(self, components):
        path = components['path']
        f = open(path)
        engine, table_engin, address_engine = StorageRegister.get_engine()
        table_engin(address_engine()).save(readline(f))
