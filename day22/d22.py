"""
Advent Of Code
--- Day 22: Monkey Map ---
https://adventofcode.com/2022/day/22
"""
from __future__ import annotations


class Problem:
    DIR = '>v<^'
    def __init__(self, input) -> None:
        self.printer = print if __debug__ else lambda *x: None
        self.board, self.path = input
        self.xy = list(self.board)[0]
        self.dir = '>'
        self.mm = dict()
        self.wrap_strategy = 1
        for (x, y) in self.board:
            # (0=row/1=col, 0=min/1=max, delta)
            if (0, 0, y) not in self.mm:
                self.mm[(0, 0, y)] = x
            else:
                self.mm[(0, 1, y)] = x
            if (1, 0, x) not in self.mm:
                self.mm[(1, 0, x)] = y
            else:
                self.mm[(1, 1, x)] = y
        self.current = 0

    def wrap(self, xy, d):
        x, y = xy
        if (x + d[0], y + d[1]) in self.board:
            return (x + d[0], y + d[1]), self.dir
        if self.wrap_strategy == 1:
            if d[1] == 0:
                j = 1 if x == self.mm[(0, 0, y)] else 0
                x = self.mm[(0, j, y)]
            else:
                j = 1 if y == self.mm[(1, 0, x)] else 0
                y = self.mm[(1, j, x)]
            dir = self.dir
        else:
            if len(self.board) == 4*4*6:
                M = 4
                zones = [
                    # position, mapping right/bottom/left/top each is (zone, rotate CCW)
                    ((2, 0), (5,180), None, (2, 270), (1, 180)),
                    ((0, 1), None, (4, 180), (5, 90), (0, 180)),
                    ((1, 1), None, (4, 270), None, (0, 90)),
                    ((2, 1), (5, 90), None, None, None),
                    ((2, 2), None, (1,180), (2, 90), None),
                    ((3, 2), (0, 180), (1, 270), None, (3, 270))
                ]
            else:
                M = 50
                zones = [
                    # position, mapping right/bottom/left/top each is (zone, rotate CCW)
                    ((1, 0), None, None, (4, 180), (5, 90)),
                    ((2, 0), (3, 180), (2, 90), None, (5, 0)),
                    ((1, 1), (1, 270), None, (4, 270), None),
                    ((1, 2), (1, 180), (5, 90), None, None),
                    ((0, 2), None, None, (0, 180), (2, 90)),
                    ((0, 3), (3, 270), (1, 0), (0, 270), None)
                ]
            for j in range(6):
                z = zones[j]
                if z[0][0] * M <= x < (z[0][0] + 1) * M and z[0][1] * M <= y < (z[0][1] + 1) * M:
                    self.printer(f'  In zone {j}')
                    break
            else:
                raise ValueError(f'Zone not found for {xy}')
            # Find neighbor
            neighbor = z[[(1,0),(0,1),(-1,0),(0,-1)].index(d)+1]
            self.printer(f'  Move to zone {neighbor[0]} {neighbor[1]}°CCW')
            zz = z[0] # zone position
            zn = zones[neighbor[0]][0] # zone position
            rn = neighbor[1] # rotate
            dx, dy = x - zz[0]*M, y - zz[1]*M # delta from zone
            sx, sy = zn[0]*M, zn[1]*M # zone border
            D = M-1
            dir = self.DIR[(self.DIR.index(self.dir) + rn//90) % 4]
            if rn == 0:
                if d[0] == 0:
                    x, y = dx + sx, sy + (0 if d[1] == 1 else D)
                elif d[1] == 0:
                    x, y = sx + (0 if d[1] == 1 else D), dy + sy
            elif rn == 90:
                if d[0] == 0:
                    x, y = sx + (0 if d[1] == -1 else D), dx + sy
                elif d[1] == 0:
                    x, y = sx + D - dy, sy + (0 if d[0] == 1 else D)
            elif rn == 180:
                if d[0] == 0:
                    x, y = sx + D - dx, sy + (0 if d[1] == -1 else D)
                elif d[1] == 0:
                    x, y = sx + (0 if d[0] == -1 else D), sy + D - dy
            elif rn == 270:
                if d[0] == 0:
                    x, y = sx + (0 if d[1] == 1 else D), sy + D - dx
                elif d[1] == 0:
                    x, y = sx + dy, sy + (0 if d[0] == -1 else D)
        self.printer(f'  Wrap {xy} {self.dir} to ({x}, {y}) {dir}')
        return (x, y), dir

    def ahead(self):
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))[self.DIR.index(self.dir)]
        return self.wrap(self.xy, d)

    def next(self):
        if self.current >= len(self.path):
            return False
        c = self.path[self.current]
        if type(c) == int:
            self.printer(f'At {self.xy}: Go ahead {c} step. Current direction {self.dir}')
            for _ in range(c):
                xy, dir = self.ahead()
                if self.board[xy] == '#':
                    break
                self.xy, self.dir = xy, dir
            self.printer(f'  current position {self.xy} {self.dir}')
        else:
            self.dir = self.DIR[(self.DIR.index(self.dir) + (-1 if c == 'L' else 1)) % 4]
            self.printer(f'At {self.xy}: turn {c}, new direction is {self.dir}')
        self.current += 1
        return True

    def solve(self):
        while self.next():
            pass
        return 1000 * (self.xy[1] + 1) + 4 * (self.xy[0] + 1) + self.DIR.index(self.dir)


class Solver:
    def __init__(self, input) -> None:
        board = {}
        path = []
        for i, line in enumerate(input):
            if not line:
                for c in input[i + 1]:
                    if c in 'LR':
                        path.append(c)
                    else:
                        c = int(c)
                        if path and type(path[-1]) == int:
                            path[-1] = path[-1] * 10 + c
                        else:
                            path.append(c)
                break
            for j in range(len(line)):
                if line[j] != ' ':
                    board[(j, i)] = line[j]
        self.input = (board, path)

    def solve(self, part=1):
        problem = Problem(self.input)
        problem.wrap_strategy = part
        return problem.solve()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().rstrip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
