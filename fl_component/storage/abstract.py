class AbstractAddress():
    pass


class AbstractTable():
    def collect(self):
        raise NotImplementedError()

    def __iter__(self):
        return self.collect()
