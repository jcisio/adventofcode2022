"""
Advent Of Code
--- Day 19: Not Enough Minerals ---
https://adventofcode.com/2022/day/19
"""
import functools
import parse


class Problem:
    MINUTES=24
    class Blueprint:
        def __init__(self, blueprint: str) -> None:
            r = parse.parse('Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.', blueprint)
            if not r:
                raise ValueError()
            self.ore = r.fixed[1]
            self.clay = r.fixed[2]
            self.obsidian = (r.fixed[3], r.fixed[4])
            self.geode = (r.fixed[5], r.fixed[6])


    def __init__(self, blueprints: list[Blueprint]) -> None:
        self.blueprints = blueprints

    def max_geodes(self, blueprint: Blueprint) -> int:
        robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
        resource = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
        m = 1
        while m <= self.MINUTES:
            print(f'== Minute {m} ==')
            print('Resource before', resource)
            print('Robots', robots)
            new_robot = None
            if resource['obsidian']+robots['obsidian'] >= blueprint.geode[1]:
                # Do not build new robot to keep ore for next one.
                # Except if it is for geode.
                if resource['ore'] >= blueprint.geode[0] and resource['obsidian'] >= blueprint.geode[1]:
                    new_robot = 'geode'
                    resource['ore'] -= blueprint.geode[0]
                    resource['obsidian'] -= blueprint.geode[1]
            elif resource['clay'] + robots['clay'] >= blueprint.obsidian[1]:
                # Do not build new robot to keep ore for next one.
                # Except if it is for obsidian
                if resource['ore'] >= blueprint.obsidian[0] and resource['clay'] >= blueprint.obsidian[1]:
                    new_robot = 'obsidian'
                    resource['ore'] -= blueprint.obsidian[0]
                    resource['clay'] -= blueprint.obsidian[1]
            elif resource['clay'] + robots['clay']*2 >= blueprint.obsidian[1]:
                if resource['ore'] + robots['ore']*2 < blueprint.obsidian[0]:
                    pass
            elif resource['ore'] >= blueprint.clay and max(resource['clay'], robots['clay']) < blueprint.obsidian[1]:
                new_robot = 'clay'
                resource['ore'] -= blueprint.clay
            elif resource['ore'] >= blueprint.obsidian[0] and resource['clay'] >= blueprint.obsidian[1]:
                new_robot = 'obsidian'
                resource['ore'] -= blueprint.obsidian[0]
                resource['clay'] -= blueprint.obsidian[1]
            elif resource['ore'] >= blueprint.geode[0] and resource['obsidian'] >= blueprint.geode[1]:
                new_robot = 'geode'
                resource['ore'] -= blueprint.geode[0]
                resource['obsidian'] -= blueprint.geode[1]
            for r in robots:
                resource[r] += robots[r]
            if new_robot:
                print(f'New robot {new_robot}')
                robots[new_robot] += 1
            print('Resource after', resource)
            m += 1
        return resource['geode']


    def solve(self):
        return self.max_geodes(self.blueprints[0])
#        return sum([(i+1)*self.max_geodes(blueprint) for i, blueprint in enumerate(self.blueprints)])


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return [Problem.Blueprint(line) for line in self.input]

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
