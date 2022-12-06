f = open(__file__[:-3] + '.in', 'r')


def solve(input):
    for i in range(len(input)-3):
        s = input[i:i+4]
        if s[0] not in s[1:] and s[1] not in s[2:] and s[2] != s[3]:
            return i+4


input = f.read().strip()
print("Puzzle 1: ", solve(input))
