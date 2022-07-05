import sys
import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
    print(dir(sys.stdout))
    p = subprocess.Popen(
        ['python3', 'run.py', '-m', 'Upload'],
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
        'urls': 'file:///Users/xinchengshao/Desktop/workspace/python-fl-runner/var/storage/2022-07-04/0e14e146eb5b475082028e443153b4e3'
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
