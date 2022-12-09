f = open(__file__[:-3] + '.in', 'r')


def nextp(h, t, m):
#    print(m)
    next = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    p = []
    n = next[m[0]]
    while True and m[1] > 0:
        m[1] -= 1
        h = [h[0]+n[0], h[1]+n[1]]
        for i in range(2):
            if abs(h[i]-t[i]) > 1:
                # need to move
                t[1-i] = h[1-i]
                d = 1 if h[i] > t[i] else -1
                for j in range(m[1]+1):
                    t[i] += d
                    p.append((t[0], t[1]))
                break
        else:
            continue
        break
    h = [h[0]+n[0]*m[1], h[1]+n[1]*m[1]]

#    print(h,t,p)
    return h, t, p


def solve(moves):
    h = [0, 0]
    t = [0, 0]
    positions = {(0, 0)}
    for m in moves:
        h, t, pos = nextp(h, t, m)
        for p in pos:
            positions.add(p)
    return len(positions)


moves = [[line[0], int(line[2:])] for line in f.read().strip().split('\n')]
print("Puzzle 1: ", solve(moves))
