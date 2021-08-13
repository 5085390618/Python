class Cell:
    def __init__(self, quan):
        self.quan = int(quan)

    def __add__(self, other):
        return self.quan + other.quan

    def __sub__(self, other):
        sub = self.quan - other.quan
        return sub if sub > 0 else 'Нет'

    def __truediv__(self, other):
        return self.quan // other.quan

    def __mul__(self, other):
        return self.quan * other.quan

    def make_order(self, row):
        result = ''
        for i in range(int(self.quan / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quan % row) + '\n'
        return result

cell_1 = Cell(8)
cell_2 = Cell(4)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell.make_order(5))
