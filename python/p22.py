def printBoundary(a, m, n):
    for i in range(m):
        for j in range(n):
            if (i == 0):
                print(a[i][j], end=" ")
            elif (i == m - 1):
                print(a[i][j], end=" ")
            elif (j == 0):
                print(a[i][j], end=" ")
            elif (j == n - 1):
                print(a[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
    m = 4
    n = 4
    printBoundary(a, m, n)
