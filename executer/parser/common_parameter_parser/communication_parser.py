from exception.executer.parser import CommonParameterParserError


class CommunicationParser():
    def __init__(self, communication_conf):
        self.communication_conf = communication_conf

    def validate(self):
        if self.communication_conf == None:
            raise CommonParameterParserError(
                msg='common_parameter.communication is required'
            )
