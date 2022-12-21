"""
Advent Of Code
--- Day 21: Monkey Math ---
https://adventofcode.com/2022/day/21
"""
from __future__ import annotations
import re

class Monkey:
    monkeys = dict()

    def __init__(self, definition) -> None:
        name, attr = definition.split(': ')
        self.name = name
        r = re.findall('[^\d ]+', attr)
        if r:
            self.op = r[1]
            self.arg = (r[0], r[2])
            self._val = None
        else:
            self.arg = ()
            self._val = int(attr)
        # Reverse dependencies
        self.dep = set()
        Monkey.monkeys[name] = self

    @staticmethod
    def find(name: str) -> Monkey:
        return Monkey.monkeys[name]

    @staticmethod
    def find_all() -> list[Monkey]:
        return Monkey.monkeys.values()

    @property
    def val(self):
        if self._val != None:
            return self._val
        if self.op == '+':
            self._val = self.find(self.arg[0]).val + self.find(self.arg[1]).val
        elif self.op == '-':
            self._val = self.find(self.arg[0]).val - self.find(self.arg[1]).val
        elif self.op == '*':
            self._val = self.find(self.arg[0]).val * self.find(self.arg[1]).val
        elif self.op == '/':
            self._val = self.find(self.arg[0]).val / self.find(self.arg[1]).val
        else:
            raise ValueError
        return self._val


class Problem:
    def __init__(self) -> None:
        self.printer = print if __debug__ else lambda *x: None

    def solve(self):
        return int(Monkey.find('root').val)

    def solve2(self):
        for m in Monkey.find_all():
            list(map(lambda a: Monkey.find(a).dep.add(m.name), m.arg))
        dep = set()
        check = set(['humn'])
        while check:
            m = check.pop()
            dep.add(m)
            check |= Monkey.find(m).dep
        root = Monkey.find('root')
        self.printer(dep)
        if root.arg[0] in dep and root.arg[1] in dep:
            raise ValueError('Can not solve easily..')
        i = 0 if root.arg[0] in dep else 1
        val = Monkey.find(root.arg[1-i]).val
        self.printer(f'Root need to yell {val}')
        m = Monkey.find(root.arg[i])
        while m.name != 'humn':
            i = 1 if m.arg[0] in dep else 0
            arg = Monkey.find(m.arg[i]).val
            self.printer(f'Inspecting monkey {m.name}: {m.arg[0]} {m.op} {m.arg[1]} value of {Monkey.find(m.arg[i]).name} is {arg}')
            if m.op == '+':
                val = val - arg
            elif m.op == '-':
                val = arg - val if i == 0 else val + arg
            elif m.op == '*':
                val = val / arg
            elif m.op == '/':
                val = arg / val if i == 0 else val * arg
            m = Monkey.find(m.arg[1-i])
            self.printer(f'{m.name} needs to yell {val}')
        return int(val)


class Solver:
    def __init__(self, input) -> None:
        self.input = [Monkey(line) for line in input]

    def solve(self, part=1):
        problem = Problem()
        return problem.solve() if part == 1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
