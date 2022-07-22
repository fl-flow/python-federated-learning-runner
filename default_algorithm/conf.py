CONF = {
    'Demo': {
        'GUEST': {
            'module': 'default_algorithm.demo.demo',
            'cls': 'Demo'
        },
        'HOST': {
            'module': 'default_algorithm.demo.demo',
            'cls': 'Demo'
        }

    },
    'DataReader': {
        'module': 'default_algorithm.reader.data_reader',
        'cls': 'Reader'
    },
    'TensorReader': {
        'module': 'default_algorithm.reader.tensor_reader',
        'cls': 'Reader'
    },
    'Upload': {
        'module': 'default_algorithm.upload',
        'cls': 'Upload'
    }
}
