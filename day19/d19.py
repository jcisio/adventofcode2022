"""
Advent Of Code
--- Day 19: Not Enough Minerals ---
https://adventofcode.com/2022/day/19
"""
from __future__ import annotations
import parse


class Problem:
    class Blueprint:
        def __init__(self, blueprint: str) -> None:
            r = parse.parse('Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.', blueprint)
            if not r:
                raise ValueError()
            self.ore = r.fixed[1]
            self.clay = r.fixed[2]
            self.obsidian = (r.fixed[3], r.fixed[4])
            self.geode = (r.fixed[5], r.fixed[6])
            self.robots = ('ore', 'clay', 'obsidian', 'geode')

        @staticmethod
        def cmp(a, b):
            '''Compare two resource'''
            for r in range(7,3,-1):
                if a[r] < b[r]:
                    return -1
                elif a[r] > b[r]:
                    return 1
            return 0

        def get_upper_bound(self, s, minutes):
            '''Return the upper bound number of geodes that could be build'''
            # If we don't have enought obsidian, build them first.
            if s[6] < self.geode[1]:
                minutes -= 1
            # Return the number if we build one geode-cracking every minute.
            return (s[3] + minutes) * (s[3] + minutes - 1) // 2 - s[3] * (s[3] - 1) // 2 + s[7]

        def add_state(self, s, m):
            if not hasattr(self, 'cache'):
                self.cache = set()
            if (s,m) in self.cache:
                return
            self.cache.add((s,m))
            self.states.append((s, m))
            if __debug__:
                print(f'-> Add state {s} {m}')

        def pop_state(self):
            s, m = self.states.pop(0)
            # if __debug__:
            #     print(f'Pop state {s} {m}')
            return (s, m)

        def max_geodes(self, minutes) -> int:
            if __debug__:
                print('Computing blueprint...')
            state_max = None
            self.states = []
            # First step is to wait and collect ore.
            # 4 robots and 4 resource
            self.add_state((1, 0, 0, 0, 0, 0, 0, 0), minutes)
            while self.states:
                s, m = self.pop_state()
                if m == 0:
                    # Last step: eval.
                    if not state_max or self.cmp(state_max, s) == -1:
                        state_max = s
                        if __debug__:
                            print(f'* Found new max of {s[7]} with state {s}')
                    continue
                # if state_max and self.get_upper_bound(s, m) <= state_max[7]:
                #     continue

                build = False
                m -= 1
                if s[4] >= self.geode[0] and s[6] >= self.geode[1]:
                    self.add_state((s[0], s[1], s[2], s[3]+1, s[0]+s[4]-self.geode[0], s[1]+s[5], s[2]+s[6]-self.geode[1], s[3]+s[7]), m)
                    build = True
                elif s[4] >= self.obsidian[0] and s[5] >= self.obsidian[1]:
                    self.add_state((s[0], s[1], s[2]+1, s[3], s[0] + s[4] - self.obsidian[0], s[1] + s[5]-self.obsidian[1], s[2] + s[6], s[3] + s[7]), m)
                    build = True
                if s[4] >= self.clay and s[1] < self.obsidian[1]:
                    self.add_state((s[0], s[1]+1, s[2], s[3], s[0] + s[4] - self.clay, s[1] + s[5], s[2] + s[6], s[3] + s[7]), m)
                    build = True
                if s[4] >= self.ore and s[0] < max(self.clay, self.obsidian[0], self.geode[0]):
                    self.add_state((s[0]+1, s[1], s[2], s[3], s[0] + s[4] - self.ore, s[1] + s[5], s[2] + s[6], s[3] + s[7]), m)
                    build = True
                if not build or s[4] <= max(self.clay, self.obsidian[0], self.geode[0]):
                    self.add_state((s[0], s[1], s[2], s[3], s[0] + s[4], s[1] + s[5], s[2] + s[6], s[3] + s[7]), m)
            return state_max[7]

    def __init__(self, blueprints: list[Blueprint]) -> None:
        self.blueprints = blueprints

    def solve(self):
#        return self.blueprints[1].max_geodes(24)
        return sum([(i+1)*blueprint.max_geodes(24) for i, blueprint in enumerate(self.blueprints)])


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return [Problem.Blueprint(line) for line in self.input]

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
# print("Puzzle 2: ", solver.solve(2))
