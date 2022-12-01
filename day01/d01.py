f = open(__file__[:-3] + '.in', 'r')


def solve(lines):
    elves = []
    current_elf = 0
    lines.append(0)
    for calorie in lines:
        if calorie == '':
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(calorie)
    return max(elves)


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solve(lines))
#print("Puzzle 2: ", solve(lines))
