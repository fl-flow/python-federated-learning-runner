import subprocess
from json import dumps
from base64 import b64encode

if __name__ == '__main__':
    p = subprocess.Popen(
        ['python3', 'run.py'],
        stdin=subprocess.PIPE
    )

    common_args = {
        'communication': {},
        'storage': {},
        'computing': {
            'engine': 'engine'
        }
    }
    task_args = {
        'arg1': 'asdasdasd'
    }
    input_length = 2
    output_length = 3

    input_data = [
        {
            'm': ['mmm'],
            'd': ['ddd'],
        },
        {
            'm': ['mmmmmm'],
            'd': ['dddddd'],
        },
    ]



    p.stdin.write(b64encode(dumps(common_args).encode()) + b'\n')
    p.stdin.write(b64encode(dumps(task_args).encode()) + b'\n')
    p.stdin.write(b64encode(f'{input_length}'.encode()) + b'\n')
    p.stdin.write(b64encode(f'{output_length}'.encode()) + b'\n')
    for i in input_data:
        p.stdin.write(b64encode(dumps(i).encode()) + b'\n')
    p.stdin.flush()

    p.wait()
