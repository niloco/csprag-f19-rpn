import operator

def factorial(n):
    result = 1

    if n == 0 or n == 1:
        return result
    else:
        for i in range(2, n + 1):
            result *= i

        return result

double_arg_ops = {
    '+':    operator.add,
    '-':    operator.sub,
    '*':    operator.mul,
    '/':    operator.floordiv,
    '%':    operator.mod,
    '**':   operator.pow,
}

single_arg_ops = {
    '!':    factorial,
}


def calculate(arg):
    stack = list()

    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            arg1 = stack.pop()
            result = 0

            try:
                function = double_arg_ops[token]
                arg0 = stack.pop()
                result = function(arg0, arg1)
            except KeyError:
                function = single_arg_ops[token]
                result = function(arg1)

            stack.append(result)

    if len(stack) > 1:
        raise TypeError('malformed input')

    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
