def calculator(a, operator, b):
    if operator == '/' and b == '0':
        raise ValueError("На ноль делить нельзя!")
    return eval(f'{a} {operator} {b}')


if __name__ == '__main__':
    try:
        while True:
            command = input()
            if command == "exit":
                break
            elif command == "easter egg":
                print("version 0.1")
            else:
                a, operator, b = command.split(' ')
                print(calculator(a, operator, b))
    except EOFError:
        print("Exception handled")
