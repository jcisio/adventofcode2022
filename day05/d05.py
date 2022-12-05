f = open(__file__[:-3] + '.in', 'r')


def parse_stacks(lines: list):
    n = (len(lines[0])+1)//4
    stacks = [[] for i in range(n)]
    line = lines.pop(0)
    while line[1] != '1':
        for i in range(n):
            if line[i*4+1] != ' ':
                stacks[i].append(line[i*4+1])
        line = lines.pop(0)

    moves = []
    for line in lines[1:]:
        items = line.split()
        moves.append([int(items[1]), int(items[3]), int(items[5])])
    return stacks, moves


def solve(stacks, moves, stack_order):
    for (n, s, t) in moves:
        v = stacks[s-1][0:n]
        stacks[s-1] = stacks[s-1][n:]
        stacks[t-1] = v[::stack_order] + stacks[t-1]
    return ''.join([stack[0] for stack in stacks])


stacks, moves = parse_stacks(f.read().rstrip().split('\n'))
print("Puzzle 1: ", solve(stacks.copy(), moves, -1))
print("Puzzle 2: ", solve(stacks, moves, 1))
