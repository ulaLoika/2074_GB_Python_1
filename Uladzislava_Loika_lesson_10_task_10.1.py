from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise ValueError ('fail initialisation matrix')

    def __str__(self):
        matrix_str = ''
        for el in self.matrix:
            el_str = ' '.join(map(str, el))
            el_str = f'| {el_str} |\n'
            matrix_str += el_str
        return matrix_str

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix[i]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print (first_matrix)
    print(first_matrix + second_matrix)
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])

