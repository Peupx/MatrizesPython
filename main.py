MatrizA = [
    [4, 3],
    [3, 6]
]
MatrizB= [
    [6, 7],
    [0, 8]
]
MatrizC = [
    [0, 0],
    [0, 0]
]

# ADIÇÃO
for i in range(2):
    for j in range(2):
        MatrizC[i][j] = MatrizA[i][j] + MatrizB[i][j]

print("Adição: ", MatrizC)

# SUBTRAÇÃO
for i in range(2):
    for j in range(2):
        MatrizC[i][j] = MatrizA[i][j] - MatrizB[i][j]

print("Subtração: ", MatrizC)

# MULTIPLICAÇÃO
for i in range(2):
    for j in range(2):
        MatrizC[i][j] = MatrizA[i][0] * MatrizB[0][j] + MatrizA[i][1] * MatrizB[1][j]

print("Multiplicação: ", MatrizC)
