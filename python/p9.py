def is_tech_number(n):
    m = str(n)
    a = m[:len(m)//2]
    b = m[len(m)//2:]
    c = int(a) + int(b)
    d = c ** 2
    return d == n

# Test the function
number_to_test = 3025  # You can replace this with any number
if is_tech_number(number_to_test):
    print("Tech number")
else:
    print("Not a Tech number")
