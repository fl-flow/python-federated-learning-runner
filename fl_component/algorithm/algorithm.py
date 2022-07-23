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

    @property
    def output_data(self):
        return self.fl_output.data

    @output_data.setter
    def output_data(self, v):
        self.fl_output.data = v

    @property
    def output_model(self):
        return self.fl_output.model

    @output_model.setter
    def output_model(self, v):
        self.fl_output.model = v

    @property
    def output_tensor(self):
        return self.fl_output.tensor

    @output_tensor.setter
    def output_tensor(self, v):
        self.fl_output.tensor = v

    @property
    def summary(self):
        return self.fl_output.summary

    @summary.setter
    def summary(self, v):
        self.fl_output.summary = v

    @property
    def output_data_ret(self):
        return self.fl_output.data_ret

    @output_data_ret.setter
    def output_data_ret(self, v):
        self.fl_output.data_ret = v

    @property
    def output_model_ret(self):
        return self.fl_output.model_ret

    @output_model_ret.setter
    def output_model_ret(self, v):
        self.fl_output.model_ret = v

    @property
    def output_tensor_ret(self):
        return self.fl_output.tensor_ret

    @output_tensor_ret.setter
    def output_tensor_ret(self, v):
        self.fl_output.tensor_ret = v
