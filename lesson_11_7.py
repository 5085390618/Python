class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%si)' % (self.a, self.b)

    def __add__(self, other):
        aa = self.a + other.a
        bb = self.b + other.b
        return ComplexNum(aa, bb)

    def __mul__(self, other):
        aa = self.a * other.a - self.b * other.b
        bb = self.b * other.a + self.a * other.b
        return ComplexNum(aa, bb)

c_1 = ComplexNum(1, 2)
c_2 = ComplexNum(2, 3)

print(f"{c_1} + {c_2} = ", c_1 + c_2)
print(f"{c_1} * {c_2} = ", c_1 * c_2)
