
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

operators = {
    '+': add,
    '-': sub,
}

def calculate(arg):
    stack = list()

    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]

            arg2 = stack.pop()
            arg1 = stack.pop()

            result = function(arg1, arg2)

            stack.append(result)

    if len(stack) > 1:
        raise TypeError('malformed input')

    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
