from .party import Party, ALL_ROLES
from .register import Register
from pickle import dumps as pickle_dumps, loads as pickle_loads


class Transfer():
    SPLIT = '?_?'

    def __init__(self, name: str, src_role: Party, dest_role: Party):
        self.name = name
        assert src_role in ALL_ROLES, f'error role {src_role}'
        assert dest_role in ALL_ROLES, f'error role {dest_role}'
        assert dest_role != src_role, f'dest_role cant be same with src_role {src_role}'
        self.src_role = src_role
        self.dest_role = dest_role

    @property
    def engine(self):
        return Register.get_engine()

    @property
    def role2party(self):
        return Register.ROLE2PARTY

    def put(self, data, tag: tuple):
        # TODO: base64
        self.engine.push(
            data=pickle_dumps(data).hex(),
            parties=self.role2party[self.dest_role],
            tag=self.name + self.SPLIT.join((str(t) for t in tag))
        )

    def get(self, tag: tuple):
        for i in self.engine.pull(
            parties=self.role2party[self.src_role],
            tag=self.name + self.SPLIT.join((str(t) for t in tag))
        ):
            yield pickle_loads(bytes.fromhex(i.decode()))
