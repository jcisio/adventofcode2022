f = open(__file__[:-3] + '.in', 'r')


def solve(input, som_length):
    for i in range(len(input)-som_length+1):
        s = input[i:i+som_length]
        if all([s[i] not in s[i+1:] for i in range(som_length-1)]):
            return i+som_length


input = f.read().strip()
print("Puzzle 1: ", solve(input, 4))
print("Puzzle 2: ", solve(input, 14))
