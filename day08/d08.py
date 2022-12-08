f = open(__file__[:-3] + '.in', 'r')


def solve(trees, next):
    # visibility from top, bottom, left, right
    visibility = [[[True, True, True, True] for tree in row] for row in trees]
    # it seems that it's a square
    L = len(trees)
    # direction
    for d in range(4):
        for i in range(1, L-1):
            if d == 0:
                current = (0, i)
            elif d == 1:
                current = (L-1, i)
            elif d == 2:
                current = (i, 0)
            else:
                current = (i, L-1)
            min = trees[current[0]][current[1]]
            for j in range(1, L-1):
                current = (current[0] + next[d][0], current[1] + next[d][1])
                if trees[current[0]][current[1]] <= min:
                    visibility[current[0]][current[1]][d] = False
                else:
                    min = trees[current[0]][current[1]]
    return sum([sum([(1 if any(visibility[i][j]) else 0) for j in range(L)]) for i in range(L)])


def solve2(trees, next):
    L = len(trees)
    maxv = 0
    for j in range(1, L-1):
        for i in range(1, L-1):
            h = trees[j][i]
            v = 1
            for d in range(4):
                distance = 0
                for k in range(1, L-1):
                    c = [j - next[d][0]*k, i - next[d][1]*k]
                    if min(c) < 0 or max(c) > L-1:
                        break
                    distance += 1
                    if trees[c[0]][c[1]] >= h:
                        break
                v = v * distance
            maxv = max(maxv, v)
    return maxv

# It would be better to use 1D array with tuple as index for easier manipulation.
trees = [list(map(int, line)) for line in f.read().strip().split('\n')]
next = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print("Puzzle 1: ", solve(trees, next))
print("Puzzle 2: ", solve2(trees, next))
