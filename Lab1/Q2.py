def product(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        return "Error: Matrices are not multipliable."

    # Initialize result matrix with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Input Matrix A
r1 = int(input("Enter number of rows of Matrix A: "))
c1 = int(input("Enter number of columns of Matrix A: "))

print("Enter elements of Matrix A:")
A = []
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

# Input Matrix B
r2 = int(input("Enter number of rows of Matrix B: "))
c2 = int(input("Enter number of columns of Matrix B: "))

print("Enter elements of Matrix B:")
B = []
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

# Calculate product
result = product(A, B)

print(result)

