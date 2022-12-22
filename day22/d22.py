"""
Advent Of Code
--- Day 22: Monkey Map ---
https://adventofcode.com/2022/day/22
"""
from __future__ import annotations
import functools
import parse


class Problem:
    def __init__(self, input) -> None:
        self.printer = print if __debug__ else lambda *x: None
        self.board, self.path = input
        self.xy = list(self.board)[0]
        self.dir = '>'
        self.mm = dict()
        for (x,y) in self.board:
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

    def ahead(self):
        d = ((-1,0),(1,0),(0,-1),(0,1))['<>^v'.index(self.dir)]
        x, y = (self.xy[0] + d[0], self.xy[1]+d[1])
        if (x, y) not in self.board:
            if d[1] == 0:
                j = 1 if x < self.mm[(0,0,y)] else 0
                x = self.mm[(0,j,y)]
            else:
                j = 1 if y < self.mm[(1,0,x)] else 0
                y = self.mm[(1,j,x)]
        return (x, y)

    def next(self):
        if self.current >= len(self.path):
            return False
        if type(self.path[self.current]) == int:
            for _ in range(self.path[self.current]):
                xy = self.ahead()
                if self.board[(xy)] == '#':
                    break
                self.xy = xy
        else:
            s = '<^>v'
            self.dir = s[(s.index(self.dir) + (-1 if self.path[self.current] == 'L' else 1)) % 4]
        self.current += 1
        return True

    def solve(self):
        while self.next():
            pass
        score = 1000 * (self.xy[1] + 1) + 4 * (self.xy[0] + 1)
        while True:
            self.xy = self.ahead()
            if self.board[self.xy] == '#':
                break
            score += 1
        return score


class Solver:
    def __init__(self, input) -> None:
        board = {}
        path = []
        mm = []
        for i, line in enumerate(input):
            if not line:
                for c in input[i+1]:
                    if c in 'LR':
                        path.append(c)
                    else:
                        c = int(c)
                        if path and type(path[-1])==int:
                            path[-1] = path[-1] * 10 + c
                        else:
                            path.append(c)
                break
            for j in range(len(line)):
                if line[j] != ' ':
                    board[(j,i)] = line[j]
        self.input = (board, path)

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().rstrip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
