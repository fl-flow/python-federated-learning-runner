import sys
import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
    print(dir(sys.stdout))
    p = subprocess.Popen(
        ['python3', 'run.py', '-m', 'Reader'],
        stdin=subprocess.PIPE
    )

    common_args = {
        'communication': {
            'engine': 'TJMQ'
        },
        'storage': {
            'engine': 'file'
        },
        'computing': {
            'engine': 'TJQueue'
        },
        'party_map': {
            'GUEST': ['127.0.0.1:8443']
        }
    }
    task_args = {
        'arg1': 'asdasdasd'
    }
    input_length = 2
    output_length = 3

    input_data = [
        {
            'annotation': 0,
            'value': dumps({
                'type': 'data',
                'value': ['file://@:/Users/xinchengshao/Desktop/workspace/python-fl-runner/var/storage/2022-06-28/99b63b5293274901ab08f514ce03b2fc?'],
            })
        },
        {
            'annotation': 0,
            'value': dumps({
                'type': 'model',
                'value': ['file://@:/Users/xinchengshao/Desktop/workspace/python-fl-runner/var/storage/2022-06-28/99b63b5293274901ab08f514ce03b2fczzz?'],
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
