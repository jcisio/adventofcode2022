"""
Advent Of Code
--- Day 24: Blizzard Basin ---
https://adventofcode.com/2022/day/24
"""
from __future__ import annotations
from collections import deque
from math import gcd


class Problem:
    def __init__(self, blizzards: list[Blizzard]) -> None:
        self.blizzards = [b for b in blizzards]
        N = Blizzard.XY[0] * Blizzard.XY[1] // gcd(Blizzard.XY[0], Blizzard.XY[1])
        self.S = []
        for _ in range(N):
            self.S.append(set(b.xy for b in self.blizzards))
            for b in self.blizzards:
                b.move()

    def can_stay(self, x, y, state, P) -> bool:
        return (x, y) not in self.S[state] and (x, y) in P

    def find(self, start, end, init_state = 0):
        P = {(x,y):1e100 for x in range(Blizzard.XY[0]) for y in range(Blizzard.XY[1])}
        P[start] = 0
        P[end] = 1e100
        Q = deque()
        Q.append(((start[0], start[1], init_state), 0))
        V = set()
        while Q:
            q, t = Q.popleft()
            if __debug__:
                print(q, t)
            V.add(q)
            P[q[:2]] = min(P[q[:2]], t)
            # Next move?
            i = (q[2]+1) % len(self.S)
            for d in [(0,0), (-1,0), (1,0), (0,-1), (0,1)]:
                if self.can_stay(q[0]+d[0], q[1]+d[1], i, P) and (q[0] + d[0], q[1] + d[1], i) not in V:
                    V.add((q[0] + d[0], q[1] + d[1], i))
                    Q.append(((q[0] + d[0], q[1] + d[1], i), t + 1))
        return P[end]

    def solve(self):
        return self.find((0, -1), (Blizzard.XY[0] - 1, Blizzard.XY[1]))

    def solve2(self):
        a, b = (0, -1), (Blizzard.XY[0] - 1, Blizzard.XY[1])
        q1 = self.find(a, b)
        q2 = self.find(b, a, q1)
        q3 = self.find(a, b, q1+q2)
        return q1 + q2 + q3


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


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
