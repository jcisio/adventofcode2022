f = open(__file__[:-3] + '.in', 'r')


def calculate_elves(lines):
    elves = []
    current_elf = 0
    lines.append(0)
    for calorie in lines:
        if calorie == '':
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(calorie)
    return elves


lines = f.read().strip().split('\n')
elves = calculate_elves(lines)
print("Puzzle 1: ", max(elves))
print("Puzzle 2: ", sum(sorted(elves)[-3:]))
