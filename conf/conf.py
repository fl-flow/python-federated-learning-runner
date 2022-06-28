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
        'module': 'fl_component.computing.engine.TJQueue.session.Session'
    },
}


STORAGE_ENGINE_MAP = {
    'file': {
        'module': {
            'table': 'fl_component.storage.engine.file.table.Table',
            'address': 'fl_component.storage.engine.file.address.Address',
        }
    }
}


PARTY_ID = 'Tho Jiajin'


ALLOWED_ROLES = ('Guest', 'Host', 'Arbiter')
