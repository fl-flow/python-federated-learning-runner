from exception.base import BaseFLError


class ExecuteRunningError(BaseFLError):
    def __init__(self, code=1000000, msg='executer running error'):
        super().__init__(
            code=code,
            msg=msg
        )
