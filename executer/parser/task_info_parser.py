from conf.conf import ALLOWED_ROLES
from exception.executer.parser import TaskInfoParserError


class TaskInfoParser():
    def __init__(self, task_info):
        self.task_info = task_info

    @property
    def job_id(self):
        return self.task_info['job_id']

    @property
    def task_id(self):
        return self.task_info['task_id']

    @property
    def role(self):
        role = self.task_info['group']
        if not (role in ALLOWED_ROLES):
            raise TaskInfoParserError(
                msg=f'illegal role ({role})'
            )
        return role

    @property
    def component(self):
        return self.task_info['task_name']
