import importlib


def import_class(instance_path):
    moudel_path, cls_name = instance_path.rsplit('.', 1)
    module = importlib.import_module(moudel_path)
    instance_cls = getattr(module, cls_name, None)
    assert instance_cls, f'模块 {instance_path} 不存在'
    return instance_cls
