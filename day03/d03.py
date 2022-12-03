f = open(__file__[:-3] + '.in', 'r')


def get_score(c):
    s = ''.join([chr(i+ord('a')) for i in range(26)] + [chr(i+ord('A')) for i in range(26)])
    return s.index(c) + 1


def solve(lines):
    score = 0
    for line in lines:
        half = len(line)//2
        for c in line[0:half]:
            if c in line[half:]:
                score += get_score(c)
                break
    return score


lines = f.read().strip().split('\n')
priorities = solve(lines)
print("Puzzle 1: ", priorities)
