def matrixmult(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n): # 0 1
        for j in range(n): # 0 1
            for k in range(n): # 0 1
                C[i][j] += A[i][k] * B[k][j]

    return C
A = [[2, 3]
    ,[4, 1]]
B = [[5, 7]
    ,[6, 8]]

print(matrixmult(A, B)[0])
print(matrixmult(A, B)[1])