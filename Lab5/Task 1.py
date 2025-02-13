class Matrix:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        result = ""
        for row in self.data:
            result += " ".join(str(x) for x in row) + "\n"
        return result.strip()

    def __add__(self, other):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                sum_product = 0
                for k in range(len(other.data)):
                    sum_product += self.data[i][k] * other.data[k][j]
                row.append(sum_product)
            result.append(row)
        return Matrix(result)

matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print("\nДодавання:")
print(matrix1 + matrix2)

print("\nВіднімання:")
print(matrix1 - matrix2)

print("\nМноження:")
print(matrix1 * matrix2)
