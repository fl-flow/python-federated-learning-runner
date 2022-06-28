import argparse

from .tracker import Tracker
from conf.conf import PARTY_ID
from .parser.parser_runner import ParserRunner
from fl_component.computing.register import Register as ComputingRegister
from fl_component.communication.register import Register as CommunicationRegister


class Executer():
    def __init__(self):
        self.parser_runner = ParserRunner()
        self.parser_runner.load()
        self.tracker = Tracker(self.parser_runner)

    def run(self):
        parser = argparse.ArgumentParser('传入参数：***.py')
        parser.add_argument('-m','--module', help='choose module')
        args = parser.parse_args()

        print(args.module)
        print(self.tracker.input_data)
        print(self.tracker.input_model)

        self.register_fl_component()
        if not args.module:
            exit(1)

    def register_fl_component(self):
        task_info = self.parser_runner.task_info
        common_parameter = self.parser_runner.common_parameter
        CommunicationRegister.register_engine(
            session_id=task_info.job_id, # TODO:
            mode=common_parameter.communication_parser.engine,
            party_map=common_parameter.party_map_parser.party_map,
            local_id=PARTY_ID,
            role=task_info.role,
        )
        self.parser_runner.task_info
        ComputingRegister.register_engine(
            session_id=task_info.job_id, # TODO: 
            mode=self.parser_runner.common_parameter.computing_parser.engine,
        )


if __name__ == '__main__':
    Executer().run()
