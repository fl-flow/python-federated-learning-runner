from pathlib import Path
from fl_component.processing.popen import Popen

CMD = f'python3 {str(Path(__file__).parent.parent.parent / "task_processing.py")}'


class Process():
    def __init__(self, target, memory, objs=None, stream=None):
        self.target = target
        self.objs = objs
        self.stream = stream
        self.memory = memory
        self.p = Popen(
            cmd=CMD,
            memory=memory,
            obj=[target] + (objs or []),
            stream=stream
        )

    def run(self):
        ret = self.p.run()
        return ret
