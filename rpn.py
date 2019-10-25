def calculate(arg):
    stack = list()

    for token in arg.split():
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        if token.isnumeric():
            stack.append(int(token))

    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
