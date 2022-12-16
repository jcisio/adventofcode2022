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


    def solve(self):
        i = 30
        rate = 0
        total = 0
        current = 'AA'
        while i > 1:
            try:
                next = max([v for v in self.valves if not self.valves[v]['open']], key=lambda v:self.valves[v]['rate']*(i - 1 - self.d[(current, v)]))
            except:
                print('Nothing')
                # Nothing else.
                total += rate*i
                break
            if i == 30: next='DD'
            d = self.d[(current, next)]
            print(f'{i} seconds left, current pressure {rate}, next is {next}, take {d} seconds to go')
            total += rate*min(d+1, i)
            if d+1 >= i:
                # Don't have time to move
                break
            i -= d + 1
            rate += self.valves[next]['rate']
            self.valves[next]['open'] = True
            current = next
        return total


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        valves = {}
        p = parse.compile('Valve {} has flow rate={:d}; {:w} {:w} to {:w} {}')
        for line in self.input:
            r = p.parse(line)
            valves[r[0]] = {'rate': r[1], 'open': False, 'next': r[5].split(', ')}
        return valves

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
