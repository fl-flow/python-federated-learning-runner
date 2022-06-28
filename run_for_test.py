import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
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
        'party_map': { # TODO:
            'GUEST': ['Tho Jiajin']
        }
    }
    task_args = {
        'arg1': 'asdasdasd'
    }
    input_length = 2
    output_length = 3

    input_data = [
        {
            'type': 'data',
            'annotation': 0,
            'value': ['file://@:/Users/xinchengshao/Desktop/workspace/python-fl-runner/var/storage/2022-06-28/99b63b5293274901ab08f514ce03b2fc?'],
        },
        {
            'type': 'model',
            'annotation': 0,
            'value': ['dddddd'],
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
        annotation = i.pop('annotation') # TODO:
        p.stdin.write(b64encode(dumps(i).encode()) + b'\n')
        p.stdin.write(b64encode(dumps(annotation).encode()) + b'\n') # TODO: write annotation
    p.stdin.flush()

    p.wait()
