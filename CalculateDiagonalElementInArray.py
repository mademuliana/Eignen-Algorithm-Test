import random

def random_matrix_and_calculate_diagonal():
    max_size = 5
    size = random.randint(2, max_size)
    matrix = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]
    print("Matrix yang digunakan adalah sebagai berikut:")
    for row in matrix:
        print(row)

    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(size):
        primary_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][size - 1 - i]

    result = primary_diagonal - secondary_diagonal
    print("\n")
    print("Hasil dari kalkulasi =", result)
