def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def find_anniversary(year):
    if is_leap_year(year):
        print(year, "is a leap year. Next Anniversary:", year + 4)
    else:
        print(year, "is not a leap year. Previous Anniversary:", year - 1)

anniversary_year = int(input("Enter the Anniversary year: "))
find_anniversary(anniversary_year)
