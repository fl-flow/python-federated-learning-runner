from functools import cached_property


class Resource():
    def __init__(self, raw_resource):
        self.raw_resource = raw_resource

    @property
    def memory(self):
        return self.raw_resource['memory']


class TaskSettingParser():
    def __init__(self, task_setting):
        self.task_setting = task_setting

    @cached_property
    def resource(self):
        return Resource(self.task_setting['resource'])
