from .storage_parser import StorageParser
from .computing_parser import ComputingParser
from .communication_parser import CommunicationParser
from exception.executer.parser import CommonParameterParserError



class CommonParameterParser():
    def __init__(self, raw):
        self.raw = raw

    def validate(self):
        if not isinstance(self.raw, dict):
            raise CommonParameterParserError(
                msg='common parameter require dict'
            )
        CommunicationParser(self.raw.get('communication')).validate()
        StorageParser(self.raw.get('storage')).validate()
        ComputingParser(self.raw.get('computing')).validate()
