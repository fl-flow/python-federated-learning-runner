import argparse

from .tracker import Tracker
from fl_component.computing.register import Register as ComputingRegister


class Executer():
    def __init__(self):
        self.tracker = Tracker()
        self.tracker.load()

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
        # communication.register.register_engine(
        #     session_id='session_id',
        #     mode=self.tracker.common_parameter.communication_parser.engine,
        # )
        ComputingRegister.register_engine(
            session_id='session_id',
            mode=self.tracker.common_parameter.computing_parser.engine,
        )


if __name__ == '__main__':
    Executer().run()
