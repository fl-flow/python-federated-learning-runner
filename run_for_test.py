import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
    p = subprocess.Popen(
        ['python3', 'run.py'],
        stdin=subprocess.PIPE
    )

    common_args = {
        'communication': {
            'engine': 'TJMQ'
        },
        'storage': {

        },
        'computing': {
            'engine': 'TJQueue'
        },
        'party_map': { # TODO:
            'Guest': ['Tho Jiajin']
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
            'value': ['file:///Users/xinchengshao/Desktop/workspace/python-fl-runner/asdasd.py'],
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
        'group': 'Guest',
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
