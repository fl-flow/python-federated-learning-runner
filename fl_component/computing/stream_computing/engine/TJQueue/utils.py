import base64
from pickle import dumps as p_dumps, loads as p_loads


def encode(data):
    return base64.b64encode(p_dumps(data))

def decode(raw):
    return p_loads(base64.b64decode(raw))