import argparse
import importlib
from functools import cached_property

from .tracker import Tracker
from conf.conf import PARTY_ID
from .parser.parser_runner import ParserRunner
from conf.conf import COMPUTING_ENGINE, STORAGE_ENGINE
from fl_component.storage.register import Register as StorageRegister
from fl_component.communication.register import Register as CommunicationRegister
from fl_component.computing.stream_computing.register import Register as ComputingRegister
from fl_component.algorithm.io import FLInput, FLOutput



class Executer():
    def __init__(self):
        parser = argparse.ArgumentParser('传入参数：***.py')
        parser.add_argument('-m','--module', help='choose module')
        parser.add_argument('-ignoreprint','--ignoreprint', help='ignore print')
        args = parser.parse_args()
        if not args.module:
            exit(1)
        if args.ignoreprint:
            from pathlib import Path
            ignore_print = Path(__file__).resolve().parent.parent / 'var'/ 'ignore_print'
            ignore_print_f = open(ignore_print, 'w')
            import builtins
            builtins.print = lambda *v: ignore_print_f.write(
                ' '.join([str(i) for i in v]) + '\n'
            ) and ignore_print_f.flush()
        self.module = args.module
        self.parser_runner = ParserRunner()
        self.parser_runner.load()
        self.tracker = Tracker(self.parser_runner)

    def run(self):

        self.register_fl_component()

        # setattr(self.algorithm, 'input_data', self.tracker.input_data)
        # setattr(self.algorithm, 'input_model', self.tracker.input_model)
        # setattr(self.algorithm, 'input_tensor', self.tracker.input_tensor)
        # setattr(self.algorithm, 'role', self.parser_runner.task_info.role)
        setattr(self.algorithm, 'fl_input', FLInput(
            **{
                'data': self.tracker.input_data,
                'model': self.tracker.input_model,
                'tensor': self.tracker.input_tensor,
                'role': self.parser_runner.task_info.role
            }
        ))
        setattr(self.algorithm, 'fl_output', FLOutput())
        # setattr(self.algorithm, 'output_data', [])
        # setattr(self.algorithm, 'output_model', [])
        # setattr(self.algorithm, 'output_tensor', [])
        # setattr(self.algorithm, 'summary', {})

        algorithm_cls = self.algorithm
        algorithm_cls.parse_parameter(self.parser_runner.parameters)
        instance = algorithm_cls()
        instance.run()
        assert isinstance(instance.summary, dict), 'error summary'
        summary_ = self.tracker.save_summary(instance.fl_output.summary)

        output_data = self.tracker.save_output_data(
            instance.fl_output.data,
            ret=instance.fl_output.data_ret
        )
        self.tracker.save_output_model(
            instance.fl_output.model,
            ret=instance.fl_output.model_ret
        )
        self.tracker.save_output_tensor(
            instance.fl_output.tensor,
            ret=instance.fl_output.tensor_ret
        )

    def register_fl_component(self):
        task_info = self.parser_runner.task_info
        session_id = f'{task_info.job_id}-{task_info.component}'
        common_parameter = self.parser_runner.common_parameter
        CommunicationRegister.register_engine(
            session_id=session_id,
            engine=common_parameter.communication_parser.engine,
            party_map=common_parameter.party_map_parser.party_map,
            local_id=PARTY_ID,
            role=task_info.role,
        )
        self.parser_runner.task_info
        ComputingRegister.register_engine(
            session_id=session_id,
            engine=COMPUTING_ENGINE,
        )
        StorageRegister.register_engine(
            session_id=session_id,
            engine=STORAGE_ENGINE
        )

    @cached_property
    def algorithm(self):

        # TODO:
        from default_algorithm.conf import CONF
        module_conf = CONF[self.module]
        if not (module_conf.get('module') and module_conf.get('cls')):
            role = self.parser_runner.task_info.role
            module_conf = module_conf.get(role)
            assert module_conf, f'error module {self.module} (role {role})'
        module = importlib.import_module(module_conf['module'])
        return getattr(module, module_conf['cls'])

if __name__ == '__main__':
    Executer().run()
