from fl_component.algorithm import BaseAlgorithm
from fl_component.computing.register import Register as ComputingRegister


class Reader(BaseAlgorithm):
    def run(self):
        # print(self.input_data)
        # print(self.input_model, 'zzz')

        for i in self.input_data:
            for j in i:
                # print(j)
                pass

        computing_session = ComputingRegister.get_engine()
        self.output_data = [
            computing_session.parallelize(
                i,
                include_key=False,
            )
            for i in [
                (1, 5, 6),
                ('a', 'b', 'c')
            ]
        ]
