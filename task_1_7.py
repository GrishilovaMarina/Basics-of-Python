class Matrix:
    def __init__(self, matr):
        self.matr = matr
    def __str__(self):
        temp = ''
        for i in range(len(self.matr)):
           temp = temp + ' '.join(map(str, self.matr[i])) + '\n'
        return temp
    def __add__(self, other):
        if len(self.matr) == len(other.matr):
            for i in range(len(self.matr)):
                if len(self.matr[i]) == len(other.matr[i]):
                    for j in range(len(self.matr[i])):
                        self.matr[i][j] = self.matr[i][j] + other.matr[i][j]
                else:
                     raise  Exception('Матрицы должны быть соразмерными')
            return Matrix(self.matr)
        else:
            raise  Exception('Матрицы должны быть соразмерными')


my_matr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matr_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(my_matr_1, '\n')
print(my_matr_2, '\n')
print(my_matr_1 + my_matr_2)