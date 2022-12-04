f = open(__file__[:-3] + '.in', 'r')


def solve(pairs):
    return sum(p[0]==p[2] or p[1]>=p[3] for p in pairs)


def solve2(pairs):
    return sum(p[0]==p[2] or p[2]<=p[1] for p in pairs)


lines = f.read().strip().split('\n')
pairs = [list(map(int, line.replace(',','-').split('-'))) for line in lines]
# Ordering.
pairs = [p if p[0]<p[2] else [p[2],p[3],p[0],p[1]] for p in pairs]
print("Puzzle 1: ", solve(pairs))
print("Puzzle 2: ", solve2(pairs))
