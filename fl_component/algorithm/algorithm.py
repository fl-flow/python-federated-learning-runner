from fl_component.algorithm.argument_parser import ArgumentParser
from exception.executer.execute_running import ExecuteRunningError


class BaseAlgorithmParameter():
    pass


class BaseAlgorithm():
    parameter = BaseAlgorithmParameter()
    Error = ExecuteRunningError

    @classmethod
    def parse_parameter(cls, raw_parameter: dict):
        ArgumentParser(
            parameter_cls=cls.parameter,
            parameter=raw_parameter
        ).parse()
