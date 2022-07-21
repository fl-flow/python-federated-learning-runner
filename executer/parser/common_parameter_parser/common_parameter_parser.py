# from .storage_parser import StorageParser
from .party_map_parser import PartyMapParser
# from .computing_parser import ComputingParser
from .communication_parser import CommunicationParser
from exception.executer.parser import CommonParameterParserError



class CommonParameterParser():
    def __init__(self, raw):
        self.raw = raw
        self.communication_parser = CommunicationParser(self.raw.get('communication'))
        self.party_map_parser = PartyMapParser(self.raw.get('party_map'))

    def validate(self):
        if not isinstance(self.raw, dict):
            raise CommonParameterParserError(
                msg='common parameter require dict'
            )
        self.communication_parser .validate()
        self.party_map_parser.validate()
