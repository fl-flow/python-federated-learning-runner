from conf.conf import COMMUNICATION_ENGINE_MAP
from exception.executer.parser import CommonParameterParserError


class CommunicationParser():
    def __init__(self, communication_conf):
        self.communication_conf = communication_conf

    def validate(self):
        if self.communication_conf == None:
            raise CommonParameterParserError(
                msg='common_parameter.communication is required'
            )
        if not(isinstance(self.communication_conf, dict)):
            raise CommonParameterParserError(
                msg='common_parameter.communication require dict'
            )
        self.engine = self.communication_conf.get('engine')
        if not self.engine:
            raise CommonParameterParserError(
                msg='common_parameter.communication.engine is required'
            )
        module = COMMUNICATION_ENGINE_MAP.get(self.engine)
        if not module:
            raise CommonParameterParserError(
                msg=f'common_parameter.computing.engine({self.engine}) is illegal'
            )
