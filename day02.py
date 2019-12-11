

input_path = 'input_test.txt'


def process(args):

    pos = 0
    op = args[pos]

    while op != 99:
        arg1 = args[pos + 1]
        arg2 = args[pos + 2]
        arg3 = args[pos + 3]
        if op == 1:
            args[arg3] = args[arg1] + args[arg2]
        else:
            args[arg3] = args[arg1] * args[arg2]

        pos += 4
        op = args[pos]

    return args[0]


def find_process_values(args):
    for x in range(100):
        for y in range(100):
            modified_args = args[:]
            modified_args[1] = x
            modified_args[2] = y
            result = process(modified_args)
            if result == 19690720:
                return f'{100 * x + y}'

    return '0000'


if __name__ == '__main__':
    with open(input_path) as input_file:
        line = input_file.readline()
        values = [int(s) for s in line.strip().split(',')]
        process_values = find_process_values(values)
        print(process_values)
