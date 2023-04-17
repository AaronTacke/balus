from abc import ABC, abstractmethod


# Models person to allow for empathetic interaction with user
class Person(ABC):
    @abstractmethod
    def should_learn(self):
        pass

    @abstractmethod
    def is_learning(self):
        pass

    @abstractmethod
    def is_relaxing(self):
        pass

    @abstractmethod
    def is_distracted(self):
        pass

    @abstractmethod
    def is_concentrated(self):
        pass

    @abstractmethod
    def is_leaving(self):
        pass

    @abstractmethod
    def is_back(self):
        pass

    @abstractmethod
    def is_happy(self):
        pass

    @abstractmethod
    def is_mad(self):
        pass
