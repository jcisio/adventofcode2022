f = open(__file__[:-3] + '.in', 'r')


def solve(trees):
    # visibility from top, bottom, left, right
    visibility = [[[True, True, True, True] for tree in row] for row in trees]
    # it seems that it's a square
    L = len(trees)
    # direction
    for d in range(4):
        for i in range(1, L-1):
            if d == 0:
                current = (0, i)
                next = (1, 0)
            elif d == 1:
                current = (L-1, i)
                next = (-1, 0)
            elif d == 2:
                current = (i, 0)
                next = (0, 1)
            else:
                current = (i, L-1)
                next = (0, -1)
            min = trees[current[0]][current[1]]
            for j in range(1, L-1):
                current = (current[0] + next[0], current[1] + next[1])
                if trees[current[0]][current[1]] <= min:
                    visibility[current[0]][current[1]][d] = False
                else:
                    min = trees[current[0]][current[1]]
    return sum([sum([(1 if any(visibility[i][j]) else 0) for j in range(L)]) for i in range(L)])


def solve2(trees):
    L = len(trees)
    maxv = 0
    for j in range(1, L-1):
        for i in range(1, L-1):
            h = trees[j][i]
            v = 1
            for d in range(4):
                if d == 0:
                    next = (1, 0)
                elif d == 1:
                    next = (-1, 0)
                elif d == 2:
                    next = (0, 1)
                else:
                    next = (0, -1)
                distance = 0
                for k in range(1, L-1):
                    c = [j - next[0]*k, i - next[1]*k]
                    if min(c) < 0 or max(c) > L-1:
                        break
                    distance += 1
                    if trees[c[0]][c[1]] >= h:
                        break
                print(j, i, d, distance)
                v = v * distance
            maxv = max(maxv, v)
    return maxv

trees = [list(map(int, line)) for line in f.read().strip().split('\n')]
print("Puzzle 1: ", solve(trees))
print("Puzzle 2: ", solve2(trees))
