x = int(input("Enter the number: "))
y = []

print("The factors of", x, "are:")
for i in range(1, x + 1):
    if x % i == 0:
        y.append(i)

print(y)
print("Number of factors:", len(y))

n = int(input("Enter N value: "))
if 1 <= n <= len(y):
    print(n, "th factor is:", y[n-1])
else:
    print("Invalid value for N.")
