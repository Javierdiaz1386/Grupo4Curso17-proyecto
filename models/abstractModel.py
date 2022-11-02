from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)
