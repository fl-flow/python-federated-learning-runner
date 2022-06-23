GUEST = 'GUEST'
HOST = 'HOST'
ARBITER = 'ARBITER'

ALL_ROLES = (
    GUEST,
    HOST,
    ARBITER,
)


class Party():
    def __init__(self, role: str, party_id: str, info: dict):
        self.role = role
        self.id = party_id
        self.info = info
