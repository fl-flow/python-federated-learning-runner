from exception.executer.parser import CommonParameterParserError


class StorageParser():
    def __init__(self, storage_conf):
        self.storage_conf = storage_conf

    def validate(self):
        if self.storage_conf == None:
            raise CommonParameterParserError(
                msg='common_parameter.storage is required'
            )
