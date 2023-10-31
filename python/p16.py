num1 = input("Enter the binary number 1: ")
num2 = input("Enter the binary number 2: ")

# Convert binary numbers to decimal, add them, and then convert the sum back to binary
binary_sum = bin(int(num1, 2) + int(num2, 2))

# Print the sum of binary numbers (excluding the '0b' prefix)
print("Sum of binary numbers:", binary_sum[2:])
