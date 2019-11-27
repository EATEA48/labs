
matrix1 = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]
           ]
a = int(input('а какое число умноджить матрицу? '))
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix1[i][j] = matrix1[i][j] * a
        print(matrix1[i][j], end=" ")
    print()