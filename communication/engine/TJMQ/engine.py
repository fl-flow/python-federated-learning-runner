import typing

from ...party import Party
from TJMQ.tj_mq.client import Client
from ..abstract import AbstractEngine


class Engine(AbstractEngine):
    def __init__(
        self,
        local_party: Party,
        ip: str,
        port: int,
        from_queue: bool=False,
        extra_info: dict={}
    ):
        self.local_party = local_party
        self.local_tjmq_client = Client(ip=ip, port=port, from_queue=from_queue)

    def pull(self, parties: typing.List[Party], tag: str):
        for p in parties:
            yield self.local_tjmq_client.pop(
                self.build_queue(
                    p,
                    self.local_party,
                    tag
                )
            )

    def push(self, data: str, parties: typing.List[Party], tag: str):
        # TODO: push to other party server
        data = data.encode()
        for p in parties:
            self.local_tjmq_client.push(
                self.build_queue(
                    self.local_party,
                    p,
                    tag
                ),
                data
            )

    def build_queue(self, former_party: Party, latter_party: Party, tag: str):
        return f'{former_party.id}{former_party.role}{tag}{latter_party.role}{latter_party.id}'
