from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Всего: {self.param / 6.5 + 0.5 + (2 * self.param + 0.3) / 100 :.2f}'

    @abstractmethod
    def abstract(self):
        pass

class Coat(Clothes):
    def consumption(self):
        return f'Пальто: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        pass

class Costume(Clothes):
    def consumption(self):
        return f'Костюм: {(2 * self.param + 0.3) / 100 :.2f} ткани'

    def abstract(self):
        pass

coat = Coat(30)
costume = Costume(30)

print(coat.consumption())
print(costume.consumption())

