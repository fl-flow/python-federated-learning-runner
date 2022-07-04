class BaseFLError(Exception):
    def __init__(self, code, msg):
        self.msg = msg
        self.code = code


# ParserError 100000
# StorageError 200000

# ExecuteRunningError 1000000
