"""
Advent Of Code
--- Day 18: Boiling Boulders ---
https://adventofcode.com/2022/day/18
"""
class Problem:
    def __init__(self, input) -> None:
        self.cubes = input
        self.delta = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

    def find_adjacent(self, cube) -> list:
        adj = [(cube[0]+x[0], cube[1]+x[1], cube[2]+x[2]) for x in self.delta]
        return [x for x in adj if x not in self.cubes]

    def solve(self):
        return sum([len(self.find_adjacent(cube)) for cube in self.cubes])

    def solve2(self):
        dim = [(min([c[i] for c in self.cubes]), max([c[i] for c in self.cubes])) for i in range(3)]
        outside = set()
        # Flood fill.
        # First by finding the cubes that we are sure that they are outside.
        for x in range(dim[0][0], dim[0][1]+1):
            for y in range(dim[1][0], dim[1][1]+1):
                outside = outside.union(set([(x,y,z) for z in dim[2] if (x,y,z) not in self.cubes]))
        for x in range(dim[0][0], dim[0][1]+1):
            for z in range(dim[2][0], dim[2][1]+1):
                outside = outside.union(set([(x, y, z) for y in dim[1] if (x, y, z) not in self.cubes]))
        for z in range(dim[2][0], dim[2][1] + 1):
            for y in range(dim[1][0], dim[1][1] + 1):
                outside = outside.union(set([(x, y, z) for x in dim[0] if (x, y, z) not in self.cubes]))
        found = True
        while found:
            found_outside = set()
            for c in outside:
                for adj in self.find_adjacent(c):
                    if all([dim[i][0] <= adj[i] <= dim[i][1] for i in range(3)]):
                        if adj not in outside:
                            found_outside.add(adj)
            found = len(found_outside) > 0
            outside = outside.union(found_outside)

        cubes = []
        for c in self.cubes:
            cubes = cubes + self.find_adjacent(c)
        return len([c for c in cubes if c in outside or any([c[i]>dim[i][1] or c[i]<dim[i][0] for i in range(3)])])


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return set([tuple(map(int, line.split(','))) for line in self.input])

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
