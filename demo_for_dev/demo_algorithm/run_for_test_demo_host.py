import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
    p = subprocess.Popen(
        ['python3', 'run.py', '-m', 'Demo'],
        stdin=subprocess.PIPE
    )

    common_args = {
        'communication': {
            'engine': 'TJMQ'
        },
        'party_map': {
            'GUEST': ['127.0.0.1:8443'],
            'HOST': ['127.0.0.1:8443']
        }
    }
    task_args = {
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
                'type': 'tensor',
                'value': [{'label': 'file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-14/fba58aa35ff4458db56c200b0e4f0af6?', 'id': 'file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-14/7cd3ba7b30ee40579b8917996b745773?', 'feature': 'file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-14/ec7667613dae4e2f929ad49edff06406?', 'meta': 'file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-14/2c98c11f039243ac9187012c9b7cddd6?'}],
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
        'group': 'HOST',
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