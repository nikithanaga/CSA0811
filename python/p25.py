def evaluate(string):
    string = string.replace(" ", "")

    def split_by(string, separators):
        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                if current:
                    lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch
        if current:
            lis.append(current)
        return lis

    def evaluate_mul_div(expression):
        lis = split_by(expression, "*/")
        result = float(lis[0])
        for i in range(1, len(lis), 2):
            operator = lis[i]
            number = float(lis[i + 1])
            if operator == "x":
                result *= number
            elif operator == "/":
                result /= number
        return result

    lis = split_by(string, "+-")
    result = evaluate_mul_div(lis[0])
    for i in range(1, len(lis), 2):
        operator = lis[i]
        number = evaluate_mul_div(lis[i + 1])
        if operator == "+":
            result += number
        elif operator == "-":
            result -= number

    return result

# Main Program
testcases = "1+2x3-4"
print(evaluate(testcases))
