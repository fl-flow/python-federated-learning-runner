import typing
from .party import Party
from conf.conf import COMMUNICATION_ENGINE_MAP
from utils.importer import import_class


class Register():
    ENGINE = None
    ROLE2PARTY = {}
    LOCAL_PARTY = None

    @classmethod
    def register_engine(
        cls,
        session_id: str,
        mode: str,
        party_map: typing.Dict[str, typing.List[str]],
        local_id: str,
        role: str
    ):
        # assert cls.ENGINE == None, 'duplicate register'
        assert mode in COMMUNICATION_ENGINE_MAP, f'error mode {mode}'
        cls.parse_party_map(party_map=party_map, local_id=local_id, role=role)
        communication_setting = COMMUNICATION_ENGINE_MAP[mode]
        cls.ENGINE = import_class(communication_setting['module'])(
            session_id=session_id,
            local_party=cls.LOCAL_PARTY,
            extra_info={},
            **communication_setting['args']
        )

    @classmethod
    def get_engine(cls):
        assert cls.ENGINE != None, 'register_engine before get_engine'
        return cls.ENGINE


    @classmethod
    def parse_party_map(
        cls,
        party_map: typing.Dict[str, typing.List[str]],
        local_id: str,
        role: str
    ):
        r = party_map.get(role, [])
        assert r, 'error role'
        assert local_id in r, 'error role local_id'
        cls.LOCAL_PARTY = Party(
            role=role,
            party_id=local_id,
            info={} # TODO:
        )
        cls.ROLE2PARTY = {
            role: [
                Party(
                    role=role,
                    party_id=i,
                    info={} # TODO:
                )
                for i in ids
            ]
            for role, ids in party_map.items()
        }
