from .storage_parser import StorageParser
from .computing_parser import ComputingParser
from .communication_parser import CommunicationParser
from exception.executer.parser import CommonParameterParserError



class CommonParameterParser():
    def __init__(self, raw):
        self.raw = raw
        self.communication_parser = CommunicationParser(self.raw.get('communication'))
        self.storage_parser = StorageParser(self.raw.get('storage'))
        self.computing_parser = ComputingParser(self.raw.get('computing'))

    def validate(self):
        if not isinstance(self.raw, dict):
            raise CommonParameterParserError(
                msg='common parameter require dict'
            )
        self.communication_parser .validate()
        self.storage_parser.validate()
        self.computing_parser.validate()
