import builtins

BUILTIN_TYPES = set(dir(builtins)) | {'NoneType'}
DEFAULT_ATTRS = set(dir(type('anonymous', tuple(), {})))


class ArgumentParser():
    def __init__(self, parameter_cls: type, parameter: dict):
        self.parameter_cls = parameter_cls
        self.parameter = parameter

    @classmethod
    def _parse(cls, parameter_cls, parameter):
        for i in (set(dir(parameter_cls)) - DEFAULT_ATTRS):
            if not (i in parameter):
                continue
            attr = getattr(parameter_cls, i)
            if type(attr).__name__ in BUILTIN_TYPES:
                setattr(parameter_cls, i, parameter[i])
                continue
            assert isinstance(parameter[i], dict), 'error # TODO: '
            cls._parse(attr, parameter[i])

    def parse(self):
        self._parse(self.parameter_cls, self.parameter)
