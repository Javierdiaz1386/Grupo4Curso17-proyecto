from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
    def __init__(self, data):
        """
        This constructor is used to transform a dictionary called data
        into an object making a flexible attributes definition
        :param data: data to convert into object
        """
        for key, value in data.items():
            setattr(self, key, value)
