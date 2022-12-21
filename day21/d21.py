"""
Advent Of Code
--- Day 21: Monkey Math ---
https://adventofcode.com/2022/day/21
"""
import functools
import re


class Problem:
    def __init__(self, input) -> None:
        self.printer = print if __debug__ else lambda *x: None
        self.monkeys = input

    def calculate(self, monkey) -> int:
        m = self.monkeys[monkey]
        if 'val' not in m:
            if m['arg'][1] == '+':
                m['val'] = self.calculate(m['arg'][0]) + self.calculate(m['arg'][2])
            elif m['arg'][1] == '-':
                m['val'] = self.calculate(m['arg'][0]) - self.calculate(m['arg'][2])
            elif m['arg'][1] == '*':
                m['val'] = self.calculate(m['arg'][0]) * self.calculate(m['arg'][2])
            elif m['arg'][1] == '/':
                m['val'] = self.calculate(m['arg'][0]) / self.calculate(m['arg'][2])
            else:
                raise ValueError
        return m['val']

    def solve(self):
        return self.calculate('root')


class Solver:
    def __init__(self, input) -> None:
        monkeys = {}
        for line in input:
            name, attr = line.split(': ')
            r = re.findall('[^\d ]+', attr)
            if r:
                monkeys[name] = {'arg': list(r)}
            else:
                monkeys[name] = {'val': int(attr)}
        self.input = monkeys

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
