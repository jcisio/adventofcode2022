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

    def find_next(self, i, current, valves):
        targets = [v for v in valves if self.d[(current,v)] < i-1]
        if not targets:
            return []
        return targets
        # The greedy solution is a good way to debug. But result is sub optimal.
        #return [max(targets, key=functools.cmp_to_key(lambda v1,v2: self.cmp(current,v1,v2)))]

    def optimize(self, rate, total, seconds, person, valves, j=0, substep=True):
        #print(f'{seconds} seconds left, current pressure {rate}, person {person}, substep {substep}')

        if seconds <= 1:
            return total + rate*seconds

        pp = person.copy()

        # If ALL are moving, in this step, just keep all moving.
        if min([p[1] for p in pp]) > 1:
            for k,p in enumerate(pp):
                pp[k] = (p[0], p[1] - 1, p[2]+1)
            return self.optimize(rate, total + rate, seconds - 1, pp, valves, j, substep)

        if substep and len(set([p[2] for p in pp])) == 1:
            # End of substep if all finish their round.
            # Update the rate for who arrived.
            for p in pp:
                if p[1] == 1:
                    rate += self.valves[p[0]]['rate'] if p[0] in self.valves else 0
            #print(f'New step. {seconds} seconds left, current pressure {rate}, person {pp}')
            return self.optimize(rate, total + rate, seconds - 1, pp, valves, j, False)

        # Otherwise, if at least one arrives at a valve. Find his new target.

        # Decide who acts first in this (sub)step? Support max=2 person.
        if len(pp) == 1:
            # Only 1
            n = 0
        else:
            # Only target j if they have not completed their substep.
            n = j if pp[j][2] <= pp[1-j][2] else 1-j

        # If this person is moving, let keep them moving and go to next person.
        if pp[n][1] > 1 :
            pp[n] = (pp[n][0], pp[n][1] - 1, pp[n][2]+1)
            return self.optimize(rate, total, seconds, pp, valves, j, True)
        else:
            # -- The most complicated part. --
            # Arrive now.
            next_valves = self.find_next(seconds, pp[n][0], valves)
            if not next_valves:
                return total + rate * seconds

            candidates = {}
            for next in next_valves:
                pp[n] = (next, self.d[(pp[n][0], next)] + 1, pp[n][2]+1)
                #print(f'Take {pp[n][1]} seconds for person {n} to {next}')
                new_valves = valves.copy()
                new_valves.remove(next)
                candidates[next] = self.optimize(rate, total, seconds, pp, new_valves, 1-n, True)
            return max(candidates.values())


    def solve(self, n, seconds):
        valves = [v for v in self.valves if self.valves[v]['rate']>0]
        #print(self.d)
        # (valve_to_go_to, time_to_arrival)
        person = [('AA', 0, 0) for _ in range(n)]
        return max([self.optimize(0, 0, seconds, person, valves, j) for j in range(n)])


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

    def solve(self, n, seconds):
        problem = Problem(self.parse_input())
        return problem.solve(n, seconds)


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve(1, 30))
#print("Puzzle 2: ", solver.solve(2, 26))
