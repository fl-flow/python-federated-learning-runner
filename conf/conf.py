COMMUNICATION_ENGINE_MAP = {
    'TJMQ': {
        'module': 'fl_component.communication.engine.TJMQ.engine.Engine',
        'args': {
            'ip': '127.0.0.1',
            'port': 5671,
            'from_queue': False
        }
    }
}

COMPUTING_ENGINE_MAP = {
    'TJQueue': {
        'module': 'fl_component.computing.stream_computing.engine.TJQueue.session.Session'
    },
}

COMPUTING_ENGINE = 'TJQueue'

STORAGE_ENGINE_MAP = {
    'file': {
        'module': {
            'table': 'fl_component.storage.engine.file.table.Table',
            'address': 'fl_component.storage.engine.file.address.Address',
        }
    }
}

STORAGE_ENGINE = 'file'

PARTY_ID = '127.0.0.1:8443'


ALLOWED_ROLES = ('GUEST', 'HOST', 'ARBITER')
