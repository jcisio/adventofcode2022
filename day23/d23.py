"""
Advent Of Code
--- Day 23: Unstable Diffusion ---
https://adventofcode.com/2022/day/23
"""
class Problem:
    def __init__(self, input) -> None:
        self.printer = print if __debug__ else lambda *x: None
        self.elves = input
        self.round = 0

    def is_empty(self, elves):
        return all(elve not in self.elves for elve in elves)

    def propose(self, elve, next):
        x,y = elve
        if self.is_empty([(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x-1,y), (x+1,y)]):
            return None
        props = [
            [(x-1,y-1), (x,y-1), (x+1,y-1)],
            [(x-1,y+1), (x,y+1), (x+1,y+1)],
            [(x-1,y-1), (x-1,y), (x-1,y+1)],
            [(x+1,y-1), (x+1,y), (x+1,y+1)]
        ]
        next = self.round
        for i in range(4):
            if self.is_empty(props[(next + i)%4]):
                return props[(next + i) % 4][1], (next + i) % 4

    def move(self):
        self.printer('== Next roundd ==')
        n = {}
        p = {}
        d = 'NSWE'
        for elve in self.elves:
            p[elve] = self.propose(elve, self.elves[elve])
            if p[elve]:
                self.printer(f'Elve {elve} proposes to move to {d[p[elve][1]]} {p[elve][0]}')
                n[p[elve][0]] = n[p[elve][0]] + 1 if p[elve][0] in n else 1
        for elve in list(self.elves):
            if p[elve]:
                if n[p[elve][0]] == 1:
                    self.printer(f'Elve {elve} moves to {d[p[elve][1]]} {p[elve][0]}')
                    self.elves[p[elve][0]] = (p[elve][1] + 1) % 4
                    del self.elves[elve]
                else:
                    self.elves[elve] = (p[elve][1] + 1) % 4
        self.round += 1
        self.print()

    def mm(self):
        M = len(self.elves) + 1000
        xmin, xmax, ymin, ymax = M, -M, M, -M
        for elve in self.elves:
            xmin = min(xmin, elve[0])
            xmax = max(xmax, elve[0])
            ymin = min(ymin, elve[1])
            ymax = max(ymax, elve[1])
        return (xmin, xmax, ymin, ymax)

    def print(self):
        xmin, xmax, ymin, ymax = self.mm()
        for y in range(ymin, ymax + 1):
            for x in range(xmin, xmax + 1):
                self.printer('NSWE'[self.elves[(x,y)]] if (x, y) in self.elves else '.', end='')
            self.printer()

    def solve(self):
        for _ in range(10):
            self.move()
        xmin, xmax, ymin, ymax = self.mm()
        return (xmax - xmin + 1) * (ymax - ymin + 1) - len(self.elves)


class Solver:
    def __init__(self, input) -> None:
        elves = {}
        for i, line in enumerate(input):
            for j, c in enumerate(line):
                if c == '#':
                    elves[(j,i)] = 0
        self.input = elves

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
