p = int(input("Enter the Principal amount: "))
n = int(input("Enter the number of years: "))
SC = input("Senior Citizen Yes/No: ")
G = input("Male/Female: ")

if SC == 'Yes' and G == 'Male':
    print("SI =", (p * n * 12) / 100)
elif SC == 'Yes' and G == 'Female':
    print("SI =", (p * n * 15) / 100)
else:
    print("SI =", (p * n * 10) / 100)
