import dicts

def calculate(arg):
    stack = list()

    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            try:
                op_type, func = dicts.operations[token]

                if op_type == dicts.fxn_type.stack:
                    stack = func(stack)
                elif op_type == dicts.fxn_type.single_arg:
                    arg = stack.pop()
                    stack.append(func(arg))
                else:
                    arg1 = stack.pop()
                    arg0 = stack.pop()
                    stack.append(func(arg0, arg1))
            except KeyError:
                raise TypeError('invalid operator')

    if len(stack) > 1:
        raise TypeError('malformed input')

    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
