"""
Advent Of Code
--- Day 21: Monkey Math ---
https://adventofcode.com/2022/day/21
"""
import re


class Problem:
    class Monkey:
        monkeys=dict()
        def __init__(self, definition) -> None:
            name, attr = definition.split(': ')
            self.name = name
            r = re.findall('[^\d ]+', attr)
            if r:
                self.op = r[1]
                self.arg = (r[0], r[2])
                self._val = None
            else:
                self._val = int(attr)
            # Reverse dependencies
            self.dep = set()
            self.monkeys[name] = self

        @staticmethod
        def get(name: str):
            return Problem.Monkey.monkeys[name]

        @property
        def val(self):
            if self._val != None:
                return self._val
            if self.op == '+':
                self._val = self.get(self.arg[0]).val + self.get(self.arg[1]).val
            elif self.op == '-':
                self._val = self.get(self.arg[0]).val - self.get(self.arg[1]).val
            elif self.op == '*':
                self._val = self.get(self.arg[0]).val * self.get(self.arg[1]).val
            elif self.op == '/':
                self._val = self.get(self.arg[0]).val / self.get(self.arg[1]).val
            else:
                raise ValueError
            return self._val

    def __init__(self) -> None:
        self.printer = print if __debug__ else lambda *x: None

    def solve(self):
        return int(Problem.Monkey.get('root').val)


class Solver:
    def __init__(self, input) -> None:
        self.input = [Problem.Monkey(line) for line in input]

    def solve(self, part=1):
        problem = Problem()
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
