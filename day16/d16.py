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
        self.clean_data()

    # Small optimization
    def clean_data(self):
        vv = list(self.d.keys())
        for v in vv:
            if v[0]==v[1]:
                del self.d[v]
            for i in range(2):
                if self.valves[v[i]]['rate']==0 and v[0]!='AA' and v in self.d:
                    del self.d[v]
        self.valves = {v:attr for v,attr in self.valves.items() if attr['rate']>0}
        # We don't care about empty valves.

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

    def cmp(self, current, v1, v2):
        diff = self.d[(current, v2)]*self.valves[v1]['rate'] - self.d[(current, v1)]*self.valves[v2]['rate']
        return -1 if diff < 0 else 1 if diff > 0 else 1

    def optimize(self, rate, total, i, current, valves):
        print(valves)
        while i > 1:
            try:
                next = max([v for v in valves if self.d[(current,v)] < i-1], key=functools.cmp_to_key(lambda v1,v2: self.cmp(current,v1,v2)))
            except:
                # Nothing else.
                total += rate * i
                break
            valves.remove(next)
            d = self.d[(current, next)]
            print(f'{i} seconds left, current pressure {rate}, take {d} seconds to {next}, open at {30+d+1-i}')
            total += rate*min(d+1, i)
            if d+1 >= i:
                # Don't have time to move
                break
            i -= d + 1
            rate += self.valves[next]['rate']
            current = next
        return total


    def solve(self):
        valves = [v for v in self.valves if self.valves[v]['rate']>0]
        return self.optimize(0, 0, 30, 'AA', valves)


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        valves = {}
        p = parse.compile('Valve {} has flow rate={:d}; {:w} {:w} to {:w} {}')
        for line in self.input:
            r = p.parse(line)
            valves[r[0]] = {'rate': r[1], 'next': r[5].split(', ')}
        return valves

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
