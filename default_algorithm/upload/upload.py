from utils.protocol_path_parser import parse
from fl_component.algorithm import BaseAlgorithm

from .parameter import Parameter
from .schema_file import FileUploader



class Upload(BaseAlgorithm):
    parameter = Parameter()
    SchemaMethodMap = {
        'file': FileUploader
    }

    def __init__(self):
        self.schema = None
        self.components = None

    def run(self):
        self.validate()
        u = self.SchemaMethodMap[self.schema](self.components).upload(self.parameter)
        self.summary.update({
            'url': u
        })

    def validate(self):
        url = self.parameter.url
        if not isinstance(url, str):
            raise self.Error(msg='url is required for upload')
        ret = parse(url)
        if not ret:
            raise self.Error(msg=f'error url {url}')
        if not (self.parameter.type in ('data', 'tensor')):
            raise self.Error(msg=f'error type {self.parameter.type}')
        schema, components = ret
        method_name = self.SchemaMethodMap.get(schema)
        if not method_name:
            raise self.Error(msg=f'error schema {url}')
        self.schema = schema
        self.components = components
