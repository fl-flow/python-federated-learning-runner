from fl_component.algorithm import BaseAlgorithm


class Reader(BaseAlgorithm):
    def run(self):
        print(self.input_data)
        print(self.input_model, 'zzz')

        for i in self.input_data:
            for j in i:
                print(j)

        self.output_data = self.input_data
