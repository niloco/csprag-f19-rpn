import dicts

def calculate(input, stack):
    result = 0

    for token in input.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            try:
                op_type, func = dicts.operations[token]

                if op_type == dicts.fxn_type.stack:
                    result = func(stack)
                elif op_type == dicts.fxn_type.single_arg:
                    arg = stack.pop()
                    result = func(arg)
                else:
                    arg1 = stack.pop()
                    arg0 = stack.pop()
                    result = func(arg0, arg1)

                stack.append(result)
            except KeyError:
                raise TypeError('invalid operator: ' + token)

    return result

def main():
    stack = list()

    while True:
        user_input = input('rpn calc> ')

        if user_input == 'print':
            print('stack: ', stack)
        elif user_input == 'clear':
            stack.clear()
        elif user_input == 'quit':
            return
        else:
            try:
                result = calculate(user_input, stack)
                print('result: ', result)
            except TypeError as e:
                print(e)

if __name__ == '__main__':
    main()
