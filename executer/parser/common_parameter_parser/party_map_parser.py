from exception.executer.parser import CommonParameterParserError
from conf.conf import PARTY_ID, COMPUTING_ENGINE_MAP, ALLOWED_ROLES


class PartyMapParser():
    def __init__(self, party_map):
        self.party_map = party_map

    def validate(self):
        if self.party_map == None:
            raise CommonParameterParserError(
                msg='common_parameter.party_map is required'
            )
        if not(isinstance(self.party_map, dict)):
            raise CommonParameterParserError(
                msg='common_parameter.party_map require dict'
            )

        for k, v in self.party_map.items():
            if not (k in ALLOWED_ROLES):
                raise CommonParameterParserError(
                    msg=f'common_parameter.party_map role {k} is illegal'
                )
            if not isinstance(v, list):
                raise CommonParameterParserError(
                    msg=f'common_parameter.party_map.role value require list'
                )
        if not (PARTY_ID in [
            party_id
            for party_ids in self.party_map.values()
            for party_id in party_ids
        ]):
            raise CommonParameterParserError(
                msg=f'local party ({PARTY_ID}) is not existed in party_map'
            )
