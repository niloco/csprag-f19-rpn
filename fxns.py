def factorial(n):
    result = 1

    if n == 0 or n == 1:
        return result
    else:
        for i in range(2, n + 1):
            result *= i

    return result

def sum(stack):
    result = 0

    while len(stack) != 0:
        result += stack.pop()

    stack.append(result)

    return result