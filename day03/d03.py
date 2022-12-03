f = open(__file__[:-3] + '.in', 'r')


def get_score(c):
    s = ''.join([chr(i+ord('a')) for i in range(26)] + [chr(i+ord('A')) for i in range(26)])
    return s.index(c) + 1

def solve1(lines):
    score = 0
    for line in lines:
        half = len(line)//2
        for c in line[0:half]:
            if c in line[half:]:
                score += get_score(c)
                break
    return score

def solve2(lines):
    score = 0
    for i in range(len(lines)//3):
        for c in lines[i*3]:
            if c in lines[i*3+1] and c in lines[i*3+2]:
                score += get_score(c)
                break
    return score


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solve1(lines))
print("Puzzle 2: ", solve2(lines))
