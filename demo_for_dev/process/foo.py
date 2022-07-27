import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


def foo(a1, a2, *stream):
    return a1, a2, [list(i) for i in stream]


from fl_component.processing import get_output_instance

def foo1(a1, a2, *stream):
    output_instance = get_output_instance()
    output_instance.output(a1)
    output_instance.output(a2)
    output_instance.output([list(i) for i in stream], stream=True)
