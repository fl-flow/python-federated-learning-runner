from functools import cached_property
from fl_component.storage.finder import Finder
from .parser.parser_runner import ParserRunner


class Tracker():
    def __init__(self, parser_runner: ParserRunner):
        self.parser_runner = parser_runner

    def _input_data(self):
        for i in self.parser_runner.input.data:
            s = i.source[i.annotation]
            yield Finder.load(s)

    @cached_property
    def input_data(self):
        return list(self._input_data())

    @cached_property
    def input_model(self):
        return [
            (i.source, i.annotation)
            for i in self.parser_runner.input.model
        ]
