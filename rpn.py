def calculate(arg):
    stack = list()

    for token in arg.split():
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append((stack.pop() - stack.pop()) * - 1) # -1 accounts for order of popping (lifo)
        elif token.isnumeric():
            if len(stack) > 1:
                raise TypeError('malformed input')
            else:
                stack.append(int(token))

    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
