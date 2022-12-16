"""
Advent Of Code
--- Day 16: Proboscidea Volcanium ---
https://adventofcode.com/2022/day/16
"""
import functools
import parse


class Problem:
    def __init__(self, valves) -> None:
        self.valves = valves
        self.current = None
        self.d = self.compute_distances()

    def compute_distances(self):
        d = {(v,v):0 for v in self.valves}
        i = 0
        while True:
            vvv = [vv for vv in d if d[vv]==i]
            found = False
            for vv in vvv:
                for n in self.valves[vv[1]]['next']:
                    if (vv[0], n) not in d:
                        d[(vv[0], n)] = i + 1
                        d[(n, vv[0])] = i + 1
                        found = True
            if not found:
                break
            i += 1
        return d

    def cmp(self, v1, v2):
        diff = self.d[(self.current, v2)]*self.valves[v1]['rate'] - self.d[(self.current, v1)]*self.valves[v2]['rate']
        return -1 if diff < 0 else 1 if diff > 0 else 1

    def solve(self):
        i = 30
        self.rate = 0
        self.total = 0
        self.current = 'AA'
        while i > 1:
            try:
                next = max([v for v in self.valves if not self.valves[v]['open']], key=functools.cmp_to_key(self.cmp))
            except:
                # Nothing else.
                self.total += self.rate*i
                break
#            if i == 28: next='BB'
            d = self.d[(self.current, next)]
            print(f'{i} seconds left, current pressure {self.rate}, take {d} seconds to {next}, open at {30+d+1-i}')
            self.total += self.rate*min(d+1, i)
            if d+1 >= i:
                # Don't have time to move
                break
            i -= d + 1
            self.rate += self.valves[next]['rate']
            self.valves[next]['open'] = True
            self.current = next
        return self.total


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        valves = {}
        p = parse.compile('Valve {} has flow rate={:d}; {:w} {:w} to {:w} {}')
        for line in self.input:
            r = p.parse(line)
            valves[r[0]] = {'rate': r[1], 'open': r[1]==0, 'next': r[5].split(', ')}
        return valves

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
