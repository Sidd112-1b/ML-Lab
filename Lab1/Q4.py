def transpose(m):
    rows = len(m)
    cols = len(m[0])

    t = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            t[j][i] = m[i][j]

    return t

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

print("Enter the matrix elements:")
m = []

for i in range(r):
    row = list(map(int, input().split()))
    m.append(row)
n=[]
n=transpose(m)
print("\n")
print(n)