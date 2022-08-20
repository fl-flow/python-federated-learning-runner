import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
    p = subprocess.Popen(
        ['python3', str(Path(__file__).resolve().parent.parent.parent / 'run.py'), '-m', 'Demo'],
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
                'value': [{"id": "file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-18/e6fd3f4b6e794f46833c8942e2079fbd?", "meta": "file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-18/9b467d2675d640e2a601b6b26fed6d4d?", "label": "file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-18/6bfb2e69b7c94c3c966fe482699d3280?", "feature": "file://@:/Users/xinchengshao/Desktop/workspace/fl/python-federated-learning-runner/var/storage/2022-08-18/78110a5a83fc440ebaae387c00138d92?"}],
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