import sys
import subprocess
from json import dumps
from pathlib import Path
from base64 import b64encode

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    p = subprocess.Popen(
        ['python3', BASE_DIR / 'run.py', '-m', 'Upload'],
        stdin=subprocess.PIPE
    )

    common_args = {
        'communication': {
            'engine': 'TJMQ'
        },
        'party_map': {
            'GUEST': ['127.0.0.1:8443']
        }
    }
    task_args = {
        'url': 'file:///Users/xinchengshao/Desktop/workspace/fl_flow/demo/operation/example/test1.csv'
    }
    input_length = 2
    output_length = 3

    input_data = [
        {
            'annotation': -1,
            'value': dumps({
                'type': 'data',
                'value': [],
            })
        },
        {
            'annotation': -1,
            'value': dumps({
                'type': 'model',
                'value': [],
            })
        },
        {
            'annotation': -1,
            'value': dumps({
                'type': 'tensor',
                'value': [],
            })
        },
    ]

    task_info = { # TODO:
        'job_id': 'job_id',
        'task_id': 'task_id',
        'group': 'GUEST',
        'task_name': 'task_name'
    }
    p.stdin.write(b64encode(dumps(task_info).encode()) + b'\n')

    p.stdin.write(b64encode(dumps(common_args).encode()) + b'\n')
    p.stdin.write(b64encode(dumps(task_args).encode()) + b'\n')
    p.stdin.write(b64encode(f'{input_length}'.encode()) + b'\n')
    p.stdin.write(b64encode(f'{output_length}'.encode()) + b'\n')
    for i in input_data:
        p.stdin.write(b64encode(dumps(i).encode()) + b'\n')
    p.stdin.flush()

    p.wait()
