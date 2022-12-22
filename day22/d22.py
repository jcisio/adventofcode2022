"""
Advent Of Code
--- Day 22: Monkey Map ---
https://adventofcode.com/2022/day/22
"""
from __future__ import annotations


class Problem:
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
        xy = (xy[0] + d[0], xy[1] + d[1])
        if xy in self.board:
            return xy, self.dir
        x, y = xy
        if self.wrap_strategy == 1:
            if d[1] == 0:
                j = 1 if x < self.mm[(0, 0, y)] else 0
                x = self.mm[(0, j, y)]
            else:
                j = 1 if y < self.mm[(1, 0, x)] else 0
                y = self.mm[(1, j, x)]
            dir = self.dir
        else:
            if d == (-1, 0):
                # A
                if 0 <= y < 50:
                    x, y = 0, 199 - y
                    dir = '>'
                # B
                elif 50 <= y < 100:
                    x, y = y - 50, 100
                    dir = 'v'
                # C
                elif 100 <= y < 150:
                    x, y = 50, 199 - y
                    dir = '<'
                # D
                elif 150 <= y:
                    x, y = y - 100, 0
                    dir = 'v'
            elif d == (1, 0):
                # E
                if 0 <= y < 50:
                    x, y = 99, 149 - y
                    dir = '<'
                # F
                elif 50 <= y < 100:
                    x, y = y, 49
                    dir = '^'
                # E again
                elif 100 <= y < 150:
                    x, y = 149, 149 - y
                    dir = '<'
                # G
                elif 150 <= y:
                    x, y = y - 100, 149
                    dir = '^'
            elif d == (0, -1):
                # B again
                if 0 <= x < 50:
                    x, y = 50, 50 + x
                    dir = '>'
                # D again
                elif 50 <= x < 100:
                    x, y = 0, 100 + x
                    dir = '>'
                # H
                elif 100 <= x < 150:
                    x, y = x - 100, 199
                    dir = '^'
            elif d == (0, 1):
                # H again
                if 0 <= x < 50:
                    x, y = x + 100, 0
                    dir = 'v'
                # G again
                elif 50 <= x < 100:
                    x, y = 49, 100 + x
                    dir = '<'
                # F again
                elif 100 <= x < 150:
                    x, y = 99, x - 50
                    dir = '<'
        self.printer(f'Wrap {xy} {d} to ({x}, {y}) {dir}')
        return (x, y), dir

    def ahead(self):
        d = ((-1, 0), (1, 0), (0, -1), (0, 1))['<>^v'.index(self.dir)]
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
            s = '<^>v'
            self.dir = s[(s.index(self.dir) + (-1 if c == 'L' else 1)) % 4]
            self.printer(f'At {self.xy}: turn {c}, new direction is {self.dir}')
        self.current += 1
        return True

    def solve(self):
        while self.next():
            pass
        score = 1000 * (self.xy[1] + 1) + 4 * (self.xy[0] + 1) + '>v<^'.index(self.dir)

        return score


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


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().rstrip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
