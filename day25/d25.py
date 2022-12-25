"""
Advent Of Code
--- Day 25: Full of Hot Air ---
https://adventofcode.com/2022/day/25
"""
from __future__ import annotations
import functools
import parse


class Problem:
    SNAFU = '=-012'

    def __init__(self, input) -> None:
        self.input = input
        pass

    @staticmethod
    def to_int(s: str) -> int:
        i = 0
        for c in s:
            i = i*5 + Problem.SNAFU.index(c) - 2
        return i

    @staticmethod
    def to_snafu(i: int) -> str:
        s = ''
        while i > 0:
            s = Problem.SNAFU[(i + 2) % 5] + s
            i = (i+2)//5
        return s
        1

    def solve(self):
        return self.to_snafu(sum(self.to_int(s) for s in self.input))

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
