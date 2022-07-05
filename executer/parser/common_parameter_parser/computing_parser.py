# from conf.conf import COMPUTING_ENGINE_MAP
# from exception.executer.parser import CommonParameterParserError
#
#
# class ComputingParser():
#     def __init__(self, computing_conf):
#         self.computing_conf = computing_conf
#
#     def validate(self):
#         if self.computing_conf == None:
#             raise CommonParameterParserError(
#                 msg='common_parameter.computing is required'
#             )
#         if not(isinstance(self.computing_conf, dict)):
#             raise CommonParameterParserError(
#                 msg='common_parameter.computing require dict'
#             )
#         self.engine = self.computing_conf.get('engine')
#         if not self.engine:
#             raise CommonParameterParserError(
#                 msg='common_parameter.computing.engine is required'
#             )
#
#         setting_conf = COMPUTING_ENGINE_MAP.get(self.engine)
#         if not setting_conf:
#             raise CommonParameterParserError(
#                 msg=f'common_parameter.computing.engine({self.engine}) is illegal'
#             )
