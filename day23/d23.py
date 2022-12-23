"""
Advent Of Code
--- Day 23: Unstable Diffusion ---
https://adventofcode.com/2022/day/23
"""
class Problem:
    def __init__(self, input) -> None:
        self.elves = input
        self.round = 0

    def is_empty(self, elves):
        return all(elve not in self.elves for elve in elves)

    def propose(self, elve):
        x,y = elve
        if self.is_empty([(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x-1,y), (x+1,y)]):
            return None
        props = [
            [(x-1,y-1), (x,y-1), (x+1,y-1)],
            [(x-1,y+1), (x,y+1), (x+1,y+1)],
            [(x-1,y-1), (x-1,y), (x-1,y+1)],
            [(x+1,y-1), (x+1,y), (x+1,y+1)]
        ]
        for i in range(4):
            if self.is_empty(props[(self.round + i)%4]):
                return props[(self.round + i) % 4][1], (self.round + i) % 4

    def move(self) -> int:
        if __debug__: print(f'== Round {self.round+1} ==')
        n = {}
        p = {}
        d = 'NSWE'
        for elve in self.elves:
            p[elve] = self.propose(elve)
            if p[elve]:
                if __debug__:
                    print(f'Elve {elve} proposes to move to {d[p[elve][1]]} {p[elve][0]}')
                n[p[elve][0]] = n[p[elve][0]] + 1 if p[elve][0] in n else 1
        moves = 0
        for elve in list(self.elves):
            if p[elve]:
                if n[p[elve][0]] == 1:
                    if __debug__:
                        print(f'Elve {elve} moves to {d[p[elve][1]]} {p[elve][0]}')
                    self.elves[p[elve][0]] = True
                    del self.elves[elve]
                    moves += 1
        self.round += 1
        if __debug__:
            self.print()
        return moves

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
                print('#' if (x, y) in self.elves else '.', end='')
            print()

    def solve(self):
        for _ in range(10):
            self.move()
        xmin, xmax, ymin, ymax = self.mm()
        return (xmax - xmin + 1) * (ymax - ymin + 1) - len(self.elves)

    def solve2(self):
        while self.move() > 0:
            pass
        return self.round


class Solver:
    def __init__(self, input) -> None:
        elves = {}
        for i, line in enumerate(input):
            for j, c in enumerate(line):
                if c == '#':
                    elves[(j,i)] = True
        self.input = elves

    def solve(self, part=1):
        problem = Problem(self.input.copy())
        return problem.solve() if part == 1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
