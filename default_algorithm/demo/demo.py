from fl_component.communication import Communication
from fl_component.algorithm import BaseAlgorithm, BaseAlgorithmParameter


class Parameter(BaseAlgorithmParameter):
    arga = None


class Demo(BaseAlgorithm):
    parameter = Parameter()
    C = Communication(src_role='GUEST', dest_role='HOST')

    def __init__(self):
        self.urls = None

    def run(self):
        if self.fl_input.role == 'GUEST':
            self.C.put(data=[0,2,5,4], tag=(1, 5, 6, 7, 8, 9), stream=True)
            # from time import sleep
            # sleep(4)
        elif self.fl_input.role == 'HOST':
            for i in list(self.C.get(tag=(1, 5, 6, 7, 8, 9))):
                print(list(i), 'zzzzzz')
            for i in self.fl_input.data:
                print(i)

            for i in self.fl_input.tensor:
                print(i)
                print(i.has_id, '(has_id)')
                print(i.has_label, '(has_label)')
                print(i.feature_names, '(feature_names)')
                print(i.id.to_numpy(), '(id tensor)')
                print(i.label.to_numpy(), '(label tensor)')
                print(i.feature.to_numpy(), '(feature tensor)')
