import queue
from threading import Thread
from fl_component.storage.register import Register as StorageRegister


IDQueue = None
LabelQueue = None
FeatureQueue = None
IDIndex = None
LabelIndex = None
FeatureNames = []
Count = {
    'label': 0,
    'id': 0,
    'feature': 0,
}
Address = {
    'label': None,
    'id': None,
    'feature': None,
    'meta': None
}

def readline(f):
    while 1:
        line = f.readline()
        if line == '':
            break
        yield line.strip().split(',')


def put_queue(item):
    item = list(item)
    id_ = item.pop(IDIndex)
    label = item.pop(LabelIndex-1)
    IDQueue.put(id_)
    LabelQueue.put(label)
    FeatureQueue.put(item)


def put_queue_without_label(item):
    item = list(item)
    id_ = item.pop(IDIndex)
    IDQueue.put(id_)
    FeatureQueue.put(item)


def gen(q, type_):
    count = 0
    data = q.get()
    global FeatureNames
    if type_ == 'feature':
        FeatureNames = data
    while 1:
        data = q.get()
        if data == '':
            break
        count += 1
        yield data
    Count[type_] = count


def storage_save_data_from_queue(queue, instance, type_):
    address = instance.save(gen(queue, type_))
    Address[type_] = address


class FileUploader():
    def __init__(self, components):
        self.components = components

    def upload(self, parameter):
        type_ = parameter.type
        if type_ == 'data':
            return self.upload_data()
        elif type_ == 'tensor':
            return self.upload_tensor(parameter.tensor_parameter)
        raise

    def upload_data(self):
        path = self.components['path']
        f = open(path)
        engine, table_engin, address_engine = StorageRegister.get_engine()
        return table_engin(address_engine()).save(readline(f))

    def upload_tensor(self, tensor_parameter):
        path = self.components['path']
        f = open(path)

        global IDIndex
        global LabelIndex
        global IDQueue
        global LabelQueue
        global FeatureQueue

        IDIndex = int(tensor_parameter.id_index)
        LabelIndex = int(tensor_parameter.label_index)

        IDQueue = queue.Queue()
        LabelQueue = queue.Queue()
        FeatureQueue = queue.Queue()

        engine, table_engin, address_engine = StorageRegister.get_engine()
        ts = [
            Thread(
                target=storage_save_data_from_queue,
                args=(IDQueue, table_engin(address_engine()), 'id')
            ),
            Thread(
                target=storage_save_data_from_queue,
                args=(FeatureQueue, table_engin(address_engine()), 'feature')
            ),
        ]
        if LabelIndex >= 0:
            ts.append(Thread(
                target=storage_save_data_from_queue,
                args=(LabelQueue, table_engin(address_engine()), 'label')
            ))
            for t in ts: t.start()
            for i in readline(f): put_queue(i)
        else:
            for t in ts: t.start()
            for i in readline(f): put_queue_without_label(i)
        IDQueue.put('')
        LabelQueue.put('')
        FeatureQueue.put('')
        for t in ts: t.join()
        if LabelIndex >= 0:
            assert Count['id'] == Count['label'] == Count['feature'], \
            f"error raw data, id.count({Count['id']}), label.count({Count['label']}), feature.count({Count['feature']})"
        else:
            assert Count['id'] == Count['feature'], \
            f"error raw data, id.count({Count['id']}),  feature.count({Count['feature']})"
        meta_ = {
            'feature_names': FeatureNames,
            'has_label': True,
            'has_id': True,
            'label_address': Address['label'],
            'id_address': Address['id'],
            'feature_address': Address['feature'],

        }
        addr = table_engin(address_engine()).save([meta_])
        Address['meta'] = addr
        return Address
