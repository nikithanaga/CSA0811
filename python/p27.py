def removeKdigits(num, k):
    stack = []

    for digit in num:
        while k > 0 and len(stack) > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # Handle the case when there are still remaining digits to be removed
    while k > 0:
        stack.pop()
        k -= 1

    result = "".join(stack).lstrip("0") or "0"
    return result

# Main Program
num = "143219"
k = 2
print(removeKdigits(num, k))
