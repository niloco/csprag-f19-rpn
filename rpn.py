import dicts

def calculate(input, stack):
    result = 0
    modified = stack.copy()

    for token in input.split():
        try:
            value = int(token)
            modified.append(value)
        except ValueError:
            try:
                op_type, func = dicts.operations[token]

                if op_type == dicts.fxn_type.stack:
                    result = func(modified)
                elif op_type == dicts.fxn_type.single_arg:
                    arg = modified.pop()
                    result = func(arg)
                else:
                    arg1 = modified.pop()
                    arg0 = modified.pop()
                    result = func(arg0, arg1)

                modified.append(result)
            except KeyError:
                raise TypeError('invalid operator: ' + token)
            except IndexError:
                raise TypeError('too few operands on stack for operator ' + token)
    
    return result, modified

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
                result, stack = calculate(user_input, stack)
                print('result: ', result)
            except TypeError as e:
                print(e)

if __name__ == '__main__':
    main()
