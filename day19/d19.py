"""
Advent Of Code
--- Day 19: Not Enough Minerals ---
https://adventofcode.com/2022/day/19
"""
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
            self.max = (None, None)

        @staticmethod
        def cmp(a, b):
            '''Compare two resource'''
            for r in ['geode', 'obsidian', 'clay', 'ore']:
                if a[r] < b[r]:
                    return -1
                elif a[r] > b[r]:
                    return 1
            return 0

        def build_robot(self, resource, option):
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
            else:
                new_robot = None
            return new_robot

        def get_upper_bound(self, robots, resource, minutes):
            '''Return the upper bound number of geodes that could be build'''
            # If we don't have enought obsidian, build them first.
            if resource['obsidian'] < self.geode[1]:
                minutes -= 1
            # Return the number if we build one geode-cracking every minute.
            N = robots['geode']
            return (N+minutes)*(N+minutes-1)//2 - N*(N-1)//2

        def build_geodes(self, robots, resource, steps, minutes):
            # Worth moving further?
            if self.max[0] and minutes <=20 and self.get_upper_bound(robots, resource, minutes) <= self.max[0]['geode']:
                pass
            resource = resource.copy()
            robots = robots.copy()
            new_robot = self.build_robot(resource, steps[-1])
            for r in robots:
                resource[r] += robots[r]
            if new_robot:
                robots[new_robot] += 1
            # And next step?
            if minutes == 1:
                if not self.max[0] or self.cmp(self.max[0], resource) == -1:
                    self.max = (resource, steps.copy())
#                    print(steps, robots, resource)
                return (robots, resource)

            options = []
            if resource['ore'] >= self.geode[0] and resource['obsidian'] >= self.geode[1]:
                options.append(4)
            else:
                if resource['ore'] >= self.obsidian[0] and resource['clay'] >= self.obsidian[1] and robots['obsidian'] < self.geode[1]:
                    options.append(3)
                if resource['ore'] >= self.clay and robots['clay'] < self.obsidian[1]:
                    options.append(2)
                if resource['ore'] >= self.ore and robots['ore'] < max(self.clay, self.obsidian[0], self.geode[0]):
                    options.append(1)
                if robots['ore'] <= min(self.clay, self.obsidian[0], self.geode[0]):
                    options.append(0)
            if not options:
                # Need to do something anyway.
                options.append(0)
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

        def print(self):
            m = 0
            robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
            resource = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
            for option in self.max[1]:
                m += 1
                print(f'== Minute {m} ==')
                new_robot = self.build_robot(resource, option)
                if option == 1:
                    print(f'Spend {self.ore} ore to start building an ore-collecting robot.')
                elif option == 2:
                    print(f'Spend {self.clay} ore to start building a clay-collecting robot.')
                elif option == 3:
                    print(f'Spend {self.obsidian[0]} ore and {self.obsidian[1]} clay to start building an obsidian-collecting robot.')
                elif option == 4:
                    print(f'Spend {self.geode[0]} ore and {self.geode[1]} obsidian to start building an geode-cracking robot.')
                for r in robots:
                    if robots[r] > 0:
                        resource[r] += robots[r]
                        print(f'{robots[r]} {r}-kissing robot collect collect {robots[r]} {r}; you now have {resource[r]} {r}.')
                if new_robot:
                    robots[new_robot] += 1
                    print(f'The new {new_robot} robot is ready, you now have {robots[new_robot]} of them.')
                print('')
            return resource['geode']

        def max_geodes(self) -> int:
            robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
            resource = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
            steps = [0]
            self.build_geodes(robots, resource, steps, Problem.MINUTES)
            return self.print()

    def __init__(self, blueprints: list) -> None:
        self.blueprints = blueprints

    def max_geodes(self, blueprint: Blueprint) -> int:
        print('Computing blueprint...')
        return blueprint.max_geodes()

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
