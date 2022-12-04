f = open(__file__[:-3] + '.in', 'r')


def solve(pairs):
    return sum((p[0]>=p[2] and p[1]<=p[3]) or (p[0]<=p[2] and p[1]>=p[3]) for p in pairs)


lines = f.read().strip().split('\n')
pairs = [list(map(int, line.replace(',','-').split('-'))) for line in lines]
print("Puzzle 1: ", solve(pairs))
