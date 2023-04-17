from .person import Person


# Homer is a naive implementation for working skeleton
class Homer(Person):
    learning = False

    def should_learn(self):
        if self.learning:
            return -1
        else:
            return 1

    def is_learning(self):
        self.learning = True

    def is_relaxing(self):
        self.learning = False

    def is_distracted(self):
        pass

    def is_concentrated(self):
        pass

    def is_leaving(self):
        pass

    def is_back(self):
        pass

    def is_happy(self):
        pass

    def is_mad(self):
        pass
