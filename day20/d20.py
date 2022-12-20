"""
Advent Of Code
--- Day 20: Grove Positioning System ---
https://adventofcode.com/2022/day/20
"""
class Problem:
    DEBUG=0
    def __init__(self, input) -> None:
        self.L = len(input)
        self.numbers = input
        # Position of L numbers:
        # current[k] is the original index of number currently at position k.
        self.current = list(range(self.L))
        self.printer = print if self.DEBUG else lambda x: None

    def print(self):
        self.printer(self.current)
        self.printer(', '.join(map(str, [self.numbers[self.current[i]] for i in range(self.L)])))

    def mix(self):
        L = len(self.numbers)
        for i, n in enumerate(self.numbers):
            k = self.current.index(i)
            j = (k + n) % (L - 1)
            if j == 0:
                j = L - 1
            if k == j:
                self.printer(f'\n{n} does not move')
            else:
                self.printer(f'\n{n} moves after {self.numbers[self.current[j if j > k else j-1]]} (position {k} moves to {j}):')
                if j < k:
                    self.current = self.current[0:j] + [self.current[k]] + self.current[j:k] + self.current[k + 1:L]
                elif j > k:
                    self.current = self.current[0:k] + self.current[k + 1:j + 1] + [self.current[k]] + self.current[j + 1:L]
            self.print()

    def solve(self, n_mix=1):
        self.print()
        for _ in range(n_mix):
            self.mix()
        j = self.current.index(self.numbers.index(0))
        self.printer(f'0 is at position {j}')
        return sum([self.numbers[self.current[(j + i) % self.L]] for i in [1000, 2000, 3000]])


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return list(map(int, self.input))

    def solve(self, part=1):
        input = self.parse_input()
        if part==1:
            problem = Problem(input)
            return problem.solve(1)

        problem = Problem(list(map(lambda x: x * 811589153, input)))
        return problem.solve(10)

f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
