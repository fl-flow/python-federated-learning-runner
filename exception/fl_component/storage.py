from exception.base import BaseFLError

class BaseStorageError(BaseFLError):
    def __init__(self, code=200000, msg='storage error'):
        super().__init__(
            code=code,
            msg=msg
        )


class StorageSourceParseError(BaseStorageError):
    def __init__(self, code=200100, msg='storage parse error'):
        super().__init__(
            code=code,
            msg=msg
        )


class StorageEngineError(BaseStorageError):
    def __init__(self, code=200200, msg='storage engine error'):
        super().__init__(
            code=code,
            msg=msg
        )
