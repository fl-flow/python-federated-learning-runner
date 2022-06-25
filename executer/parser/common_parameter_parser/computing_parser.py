from exception.executer.parser import CommonParameterParserError


class ComputingParser():
    def __init__(self, computing_conf):
        self.computing_conf = computing_conf

    def validate(self):
        if self.computing_conf == None:
            raise CommonParameterParserError(
                msg='common_parameter.computing is required'
            )
        if not(isinstance(self.computing_conf, dict)):
            raise CommonParameterParserError(
                msg='common_parameter.computing require dict'
            )
        if not('engine' in self.computing_conf):
            raise CommonParameterParserError(
                msg='common_parameter.computing.engine is required'
            )
