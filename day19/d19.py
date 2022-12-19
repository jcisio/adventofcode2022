"""
Advent Of Code
--- Day 19: Not Enough Minerals ---
https://adventofcode.com/2022/day/19
"""
import functools
import parse


class Problem:
    MINUTES = 24

    class Blueprint:
        def __init__(self, blueprint: str) -> None:
            r = parse.parse('Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.', blueprint)
            if not r:
                raise ValueError()
            self.ore = r.fixed[1]
            self.clay = r.fixed[2]
            self.obsidian = (r.fixed[3], r.fixed[4])
            self.geode = (r.fixed[5], r.fixed[6])
            self.max = None

        @staticmethod
        def cmp(a, b):
            '''Compare two resource'''
            for r in ['geode', 'obsidian', 'clay', 'ore']:
                if a[r] < b[r]:
                    return -1
                elif a[r] > b[r]:
                    return 1
            return 0

        def build_geodes(self, robots, resource, steps, minutes):
            new_robot = None
            resource = resource.copy()
            robots = robots.copy()
            option = steps[-1]
            if option == 1:
                new_robot = 'ore'
                resource['ore'] -= self.ore
            elif option == 2:
                new_robot = 'clay'
                resource['ore'] -= self.clay
            elif option == 3:
                new_robot = 'obsidian'
                resource['ore'] -= self.obsidian[0]
                resource['clay'] -= self.obsidian[1]
            elif option == 4:
                new_robot = 'geode'
                resource['ore'] -= self.geode[0]
                resource['obsidian'] -= self.geode[1]
            for r in robots:
                resource[r] += robots[r]
            if new_robot:
                robots[new_robot] += 1
            # And next step?
            if minutes == 1:
                if not self.max or self.cmp(self.max, resource) == -1:
                    self.max = resource
                    print(steps, robots, resource)
                return (robots, resource)

            options = []
            if resource['ore'] >= self.geode[0] and resource['obsidian'] >= self.geode[1]:
                options.append(4)
            elif resource['ore'] >= self.obsidian[0] and resource['clay'] >= self.obsidian[1]:
                options.append(3)
            else:
                options.append(0)
                if resource['ore'] >= self.clay:
                    options.append(2)
            max_geodes = 0
            for option in options:
                steps.append(option)
                new_robots, new_resource = self.build_geodes(robots, resource, steps, minutes - 1)
                if max_geodes <= new_resource['geode']:
                    max_robots = new_robots
                    max_resource = new_resource
                    max_geodes = new_resource['geode']
                steps.pop()
            return (max_robots, max_resource)

        def max_geodes(self) -> int:
            robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
            resource = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
            steps = [0]
            return self.build_geodes(robots, resource, steps, Problem.MINUTES)

    def __init__(self, blueprints: list[Blueprint]) -> None:
        self.blueprints = blueprints

    def max_geodes(self, blueprint: Blueprint) -> int:
        print(blueprint.max_geodes())
        return 0

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
# print("Puzzle 2: ", solver.solve(2))
