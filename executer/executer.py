import argparse

from .tracker import Tracker


class Executer():
    def __init__(self):
        pass
        self.tracker = Tracker()

    def run(self):
        parser = argparse.ArgumentParser('传入参数：***.py')
        parser.add_argument('-m','--module', help='choose module')
        args = parser.parse_args()
        print(args.module)
        if not args.module:
            exit(1)


if __name__ == '__main__':
    Executer().run()
