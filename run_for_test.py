import sys
import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
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
        'url': 'file:///Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/test1.csv'
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
        'url': 'file:///Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/test1.csv',
        'type': 'tensor',
        'tensor_parameter': {
            'id_index': 0,
            'label_index': 1
        }
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



    p = subprocess.Popen(
        ['python3', 'run.py', '-m', 'DataReader'],
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
        'urls': 'file:///Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-14/91d45f66e17946f2ae010406de8427a5'
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