import typing
from uuid import uuid4
from pickle import dumps as pickle_dumps, loads as pickle_loads

from ...party import Party
from TJMQ.tj_mq.client import Client
from ..abstract import AbstractEngine


class Engine(AbstractEngine):
    def __init__(
        self,
        session_id: str,
        local_party: Party,
        ip: str,
        port: int,
        from_queue: bool=False,
        extra_info: dict={}
    ):
        self.session_id = session_id
        self.local_party = local_party
        self.local_tjmq_client = Client(ip=ip, port=port, from_queue=from_queue)

    def pull(self, parties: typing.List[Party], tag: str):
        for p in parties:
            queue_name = self.build_queue(
                former_party=p,
                latter_party=self.local_party,
                tag=tag
            )
            h = self.pull_item(queue_name=queue_name)
            if not h.get('stream'):
                yield self.pull_item(queue_name=queue_name)
            else:
                yield self.pull_stream(header=h, queue_name=queue_name)

    def pull_stream(self, header: dict, queue_name: str):
        boundary = header.get('boundary')
        while 1:
            data = self.pull_item(queue_name)
            if data == boundary:
                break
            yield data

    def pull_item(self, queue_name):
        data = self.local_tjmq_client.pop(queue_name)
        return pickle_loads(data)

    def push(self, data, parties: typing.List[Party], tag: str, stream=False):
        # TODO: push to other party server
        if not stream:
            for p in parties:
                queue_name = self.build_queue(
                    former_party=self.local_party,
                    latter_party=p,
                    tag=tag
                )
                self.push_item(
                    queue_name=queue_name,
                    data={
                        'stream': False,
                    }
                )
                self.push_item(
                    queue_name=queue_name,
                    data=data
                )
            return
        for p in parties:
            queue_name = self.build_queue(
                former_party=self.local_party,
                latter_party=p,
                tag=tag
            )
            # TODO: new thread
            self.push_stream(queue_name, data)

    def push_stream(self, queue_name, data):
        boundary = uuid4().hex
        self.push_item(
            queue_name=queue_name,
            data={
                'stream': True,
                'boundary': boundary
            }
        )
        for i in data:
            self.push_item(
                queue_name=queue_name,
                data=i
            )
        self.push_item(
            queue_name=queue_name,
            data=boundary
        )

    def push_item(self, queue_name, data):
        data = pickle_dumps(data)
        self.local_tjmq_client.push(
            queue_name,
            data
        )

    def build_queue(self, former_party: Party, latter_party: Party, tag: str):
        return f'{self.session_id}{former_party.id}{former_party.role}{tag}{latter_party.role}{latter_party.id}'
