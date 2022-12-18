"""
Advent Of Code
--- Day 18: Boiling Boulders ---
https://adventofcode.com/2022/day/18
"""
class Problem:
    D = 3
    def __init__(self, input) -> None:
        self.cubes = input
        self.delta = []
        for i in range(self.D):
            for j in [-1, 1]:
                l = [0]*self.D
                l[i] = j
                self.delta.append(tuple(l))

    def find_adjacent(self, cube) -> list:
        adj = [tuple([cube[j]+x[j] for j in range(self.D)]) for x in self.delta]
        return [x for x in adj if x not in self.cubes]

    def solve(self):
        return sum([len(self.find_adjacent(cube)) for cube in self.cubes])

    def solve2(self):
        # Strict outer bounds.
        dim = [(min([c[i] for c in self.cubes])-1, max([c[i] for c in self.cubes])+1) for i in range(self.D)]
        # Flood fill.
        # First by finding the cubes that we are sure that they are outside.
        outside = set([tuple([dim[j][0] for j in range(self.D)])])
        found = True
        while found:
            found_outside = set()
            for c in outside:
                for adj in self.find_adjacent(c):
                    if all([dim[i][0] <= adj[i] <= dim[i][1] for i in range(self.D)]) and adj not in outside:
                        found_outside.add(adj)
            found = len(found_outside) > 0
            outside |= found_outside

        cubes = []
        for c in self.cubes:
            cubes = cubes + self.find_adjacent(c)
        return len([c for c in cubes if c in outside])


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return set([tuple(map(int, line.split(','))) for line in self.input])

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve() if part == 1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
