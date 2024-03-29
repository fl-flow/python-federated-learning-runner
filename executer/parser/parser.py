import typing
from json import loads, dumps

from .io_parser import Input, Output
from .task_info_parser import TaskInfoParser
from .task_output_annotation_parser import TaskOutputAnnotationParser
from .task_setting_parser import TaskSettingParser
from .common_parameter_parser.common_parameter_parser import CommonParameterParser


class Parser():
    def deserialize_input_data(
        self,
        raw_inputs: typing.List[str]
    ) -> typing.List[Input]:
        return Input(raw_inputs)

    def serialize_output_data(
        self,
        outputs: typing.List[Output]
    ) -> typing.List[str]:
        pass
        # return [
        #     dumps(i.build_output())
        #     for i in outputs
        # ]

    def parse_output_annotations(self, raw_output_annotations):
        return TaskOutputAnnotationParser(raw_output_annotations)

    def parse_parameter(self, raw_parameters):
        return loads(raw_parameters)

    def parse_common_parameter(self, raw_common_parameter):
        raw = loads(raw_common_parameter)
        common_parameter_parser = CommonParameterParser(raw)
        common_parameter_parser.validate()
        return common_parameter_parser

    def parse_task_info(self, task_info):
        task_info = loads(task_info)
        return TaskInfoParser(task_info)

    def parse_task_setting(self, task_setting):
        task_setting = loads(task_setting)
        return TaskSettingParser(task_setting)

