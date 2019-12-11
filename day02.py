

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


if __name__ == '__main__':
    with open(input_path) as input_file:
        line = input_file.readline()
        result = process([int(s) for s in line.strip().split(',')])
        print(result)
