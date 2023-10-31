def happy(n):
    temp = n
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum = digit ** 2 + total_sum
        temp = temp // 10
    return total_sum

# Main Program
num = int(input("Enter the number: "))
result = num

while result != 1 and result != 4:
    result = happy(result)

if result == 1:
    print("True")
elif result == 4:
    print("False")
