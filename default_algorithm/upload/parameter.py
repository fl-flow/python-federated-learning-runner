from fl_component.algorithm import BaseAlgorithmParameter


class TensorParameter():
    id_index = 0
    label_index = -1


class Parameter(BaseAlgorithmParameter):
    url = None
    type = 'data'
    tensor_parameter = TensorParameter()
