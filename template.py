import functools
import parse


class Problem:
    DEBUG=0
    def __init__(self, input) -> None:
        self.printer = print if self.DEBUG else lambda x: None

    def solve(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def parse_input(self):
        return self.input

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
