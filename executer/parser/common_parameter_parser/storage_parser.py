# from conf.conf import STORAGE_ENGINE_MAP
# from exception.executer.parser import CommonParameterParserError
#
#
# class StorageParser():
#     def __init__(self, storage_conf):
#         self.storage_conf = storage_conf
#         self.engine = None
#
#     def validate(self):
#         if self.storage_conf == None:
#             raise CommonParameterParserError(
#                 msg='common_parameter.storage is required'
#             )
#         if not isinstance(self.storage_conf, dict):
#             raise CommonParameterParserError(
#                 msg='common_parameter.storage require dict'
#             )
#         self.engine = self.storage_conf.get('engine')
#         if not self.engine:
#             raise CommonParameterParserError(
#                 msg='common_parameter.storage.engine is required'
#             )
#
#         module = STORAGE_ENGINE_MAP.get(self.engine)
#         if not module:
#             raise CommonParameterParserError(
#                 msg=f'common_parameter.storage.engine({self.engine}) is invalid'
#             )
