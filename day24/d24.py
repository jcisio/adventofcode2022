"""
Advent Of Code
--- Day 24: Blizzard Basin ---
https://adventofcode.com/2022/day/24
"""
from __future__ import annotations
from collections import deque
import functools
from math import gcd
import parse


class Problem:
    def __init__(self, blizzards: list[Blizzard]) -> None:
        self.blizzards = [b for b in blizzards]

    @staticmethod
    def can_stay(x, y, S, P) -> bool:
        return (x, y) not in S and (x, y) in P

    def solve(self):
        N = Blizzard.XY[0] * Blizzard.XY[1] // gcd(Blizzard.XY[0], Blizzard.XY[1])
        S = []
        for _ in range(N):
            S.append(set(b.xy for b in self.blizzards))
            for b in self.blizzards:
                b.move()
        P = {(x,y):1e100 for x in range(Blizzard.XY[0]) for y in range(Blizzard.XY[1])}
        P[(0, -1)] = 0
        P[(Blizzard.XY[0] - 1, Blizzard.XY[1])] = 1e100
        Q = deque()
        Q.append(((0, -1, 0), 0))
        V = set()
        while Q:
            q, t = Q.popleft()
            if __debug__:
                print(q, t)
            V.add(q)
            P[q[:2]] = min(P[q[:2]], t)
            # Next move?
            i = (q[2]+1) % N
            for d in [(0,0), (-1,0), (1,0), (0,-1), (0,1)]:
                if self.can_stay(q[0]+d[0], q[1]+d[1], S[i], P) and (q[0] + d[0], q[1] + d[1], i) not in V:
                    V.add((q[0] + d[0], q[1] + d[1], i))
                    Q.append(((q[0] + d[0], q[1] + d[1], i), t + 1))
        return P[(Blizzard.XY[0] - 1, Blizzard.XY[1])]

    def solve2(self):
        return 0


class Blizzard:
    XY = (1,1)
    def __init__(self, x, y, d) -> None:
        self.xy = (x,y)
        self.d = [(1,0),(0,1),(-1,0),(0,-1)]['>v<^'.index(d)]

    def move(self):
        self.xy = tuple([(self.xy[j] + self.d[j]) % self.XY[j] for j in range(2)])


class Solver:
    def __init__(self, input) -> None:
        b = []
        Blizzard.XY = (len(input[0])-2, len(input)-2)
        for j in range(1, len(input)-1):
            for i in range(1, len(input[j])-1):
                if input[j][i] != '.':
                    b.append(Blizzard(i-1, j-1, input[j][i]))
        self.input = b

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
