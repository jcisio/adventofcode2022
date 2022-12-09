f = open(__file__[:-3] + '.in', 'r')


def follow(h, t):
    for i in range(2):
        if abs(h[i]-t[i]) > 1:
            # Need to move because the tail is not next to the head.
            for j in range(2):
                t[j] += 1 if h[j] > t[j] else -1 if h[j] < t[j] else 0
            break
    return t

# Move t *one* step in the direction.
def move(h, t, d):
    next = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    n = next[d]
    h = [h[0]+n[0], h[1]+n[1]]
    t = follow(h, t)
    return h, t


def print_knots(knots):
    print(knots)
    X1 = min(0, min([k[0] for k in knots]))
    X2 = max([k[0] for k in knots])
    Y1 = min(0, min([k[1] for k in knots]))
    Y2 = max([k[1] for k in knots])
    for y in range(Y2-Y1+1):
        for x in range(X2-X1+1):
            try:
                i = knots.index([x+X1, Y2-y])
                print('H' if i==0 else i, end='')
            except ValueError:
                print('.', end='')
        print()


def solve(moves, n):
    knots = [[0,0] for _ in range(n)]
    positions = {(0, 0)}
    for m in moves:
        for _ in range(m[1]):
            knots[0], knots[1] = move(knots[0], knots[1], m[0])
            for i in range(2,n):
                knots[i] = follow(knots[i-1], knots[i])
            positions.add((knots[-1][0], knots[-1][1]))
#        print_knots(knots)
#    print_knots(knots)
    return len(positions)


moves = [[line[0], int(line[2:])] for line in f.read().strip().split('\n')]
print("Puzzle 1: ", solve(moves, 2))
print("Puzzle 2: ", solve(moves, 10))
