import functools


class Problem:
    def __init__(self) -> None:
        pass


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        self.problem = None
        pass

    def parse_input(self):
        return self.input

    def solve(self, part=1):
        self.problem = Problem(self.parse_input())
        return 0


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
