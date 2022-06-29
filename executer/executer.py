import argparse
import importlib
from functools import cached_property

from .tracker import Tracker
from conf.conf import PARTY_ID
from .parser.parser_runner import ParserRunner
from fl_component.storage.register import Register as StorageRegister
from fl_component.computing.register import Register as ComputingRegister
from fl_component.communication.register import Register as CommunicationRegister


class Executer():
    def __init__(self):
        parser = argparse.ArgumentParser('传入参数：***.py')
        parser.add_argument('-m','--module', help='choose module')
        args = parser.parse_args()
        if not args.module:
            exit(1)
        self.module = args.module
        self.parser_runner = ParserRunner()
        self.parser_runner.load()
        self.tracker = Tracker(self.parser_runner)

    def run(self):


        self.register_fl_component()

        setattr(self.algorithm, 'input_data', self.tracker.input_data)
        setattr(self.algorithm, 'input_model', self.tracker.input_model)
        setattr(self.algorithm, 'output_data', [])
        setattr(self.algorithm, 'output_model', [])
        instance = self.algorithm()
        instance.run()

        output_data = self.tracker.save_output_data(instance.output_data)
        self.tracker.save_output_model(instance.output_model)

    def register_fl_component(self):
        task_info = self.parser_runner.task_info
        session_id = task_info.job_id
        common_parameter = self.parser_runner.common_parameter
        CommunicationRegister.register_engine(
            session_id=session_id, # TODO:
            engine=common_parameter.communication_parser.engine,
            party_map=common_parameter.party_map_parser.party_map,
            local_id=PARTY_ID,
            role=task_info.role,
        )
        self.parser_runner.task_info
        ComputingRegister.register_engine(
            session_id=session_id, # TODO:
            engine=self.parser_runner.common_parameter.computing_parser.engine,
        )
        StorageRegister.register_engine(
            session_id=session_id,
            engine=self.parser_runner.common_parameter.storage_parser.engine
        )

    @cached_property
    def algorithm(self):

        # TODO:
        from default_algorithm.conf import CONF
        module_conf = CONF[self.module]

        module = importlib.import_module(module_conf['module'])
        return getattr(module, module_conf['cls'])

if __name__ == '__main__':
    Executer().run()
