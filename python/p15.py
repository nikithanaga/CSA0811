num = input("Enter the binary number: ")
bin_num = "01"

binary = True
for i in range(len(num)):
    if num[i] not in bin_num:
        print("Invalid input")
        binary = False
        break

if binary:
    dec_number = int(num, 2)
    oct_number = oct(dec_number)
    hexa = hex(dec_number)

    print("Decimal Equivalent =", dec_number)
    print("Octal Equivalent =", oct_number)
    print("Hexadecimal Equivalent =", hexa)
