"""
Advent Of Code
--- Day 15: Beacon Exclusion Zone ---
https://adventofcode.com/2022/day/15
"""
import functools
import re


class Problem:
    def __init__(self, sensors) -> None:
        self.sensors = sensors
        for i in range(len(self.sensors)):
            self.sensors[i].append(self.distance(self.sensors[i]))

    @staticmethod
    def distance(sensor):
        return abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])

    def draw_line(self, n):
        m = set()
        b = set()
        for s in self.sensors:
            if s[3] == n:
                b.add(s[2])
            if abs(s[1] - n) < s[4]:
                d = s[4] - abs(s[1] - n)
                for i in range(s[0] - d, s[0] + d + 1):
                    m.add(i)
        #print(m, b)
        return len(m) - len(b)


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        self.problem = None
        pass

    def parse_input(self):
        return [list(map(int, re.findall(r'\d+', x))) for x in self.input]

    def solve(self, part=1):
        self.problem = Problem(self.parse_input())
        return self.problem.draw_line(2000000)


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
