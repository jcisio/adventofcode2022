f = open(__file__[:-3] + '.in', 'r')


def solve(trees):
    # visibility from top, bottom, left, right
    visibility = [[[True, True, True, True] for tree in row] for row in trees]
    # direction
    for d in range(4):
        # it seems that it's a square
        L = len(trees)
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


trees = [list(map(int, line)) for line in f.read().strip().split('\n')]
print("Puzzle 1: ", solve(trees))
