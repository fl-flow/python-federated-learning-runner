from exception.base import BaseFLError

class BaseParserError(BaseFLError):
    def __init__(self, code=100000, msg='parser error'):
        super().__init__(
            code=code,
            msg=msg
        )


class CommonParameterParserError(BaseParserError):
    def __init__(self, code=101000, msg='common parameter parser error'):
        super().__init__(
            code=code,
            msg=msg
        )
