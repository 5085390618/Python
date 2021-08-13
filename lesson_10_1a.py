class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f"{i:3}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])

print(matrix_1 + matrix_2)
