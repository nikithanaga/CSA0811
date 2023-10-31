a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rows = len(a)
cols = len(a[0])


for i in range(rows):
    sumRow = 0
    for j in range(cols):
        sumRow += a[i][j]
    print("Sum of row", i + 1, ":", sumRow)


for i in range(cols):
    sumCol = 0
    for j in range(rows):
        sumCol += a[j][i]
    print("Sum of column", i + 1, ":", sumCol)


diagonal_sum = 0
for k in range(rows):
    diagonal_sum += a[k][k]
print("Diagonal sum:", diagonal_sum)
