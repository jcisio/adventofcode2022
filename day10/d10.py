f = open(__file__[:-3] + '.in', 'r')


def solve(lines):
    start, steps, count = 20, 40, 6
    v, s, cycle, next = 1, 0, 1, start
    print(cycle, v)
    for line in lines:
        ins = line.split()
        if ins[0] == 'noop':
            cycle += 1
        else:
            cycle += 2
        if cycle > next:
#            print('OK', cycle, v)
            s += v * next
            next += steps
            if next > start + steps*(count-1):
                break
        if ins[0] == 'addx':
            v += int(ins[1])
#        print(cycle, v)
    return s


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solve(lines))
