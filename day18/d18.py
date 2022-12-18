"""
Advent Of Code
--- Day 18: Boiling Boulders ---
https://adventofcode.com/2022/day/18
"""
class Problem:
    def __init__(self, input) -> None:
        self.cubes = input
        self.d = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

    def find_adjacent(self, cube) -> list:
        adj = [(cube[0]+x[0], cube[1]+x[1], cube[2]+x[2]) for x in self.d]
        return [x for x in adj if x not in self.cubes]

    def solve(self):
        return sum([len(self.find_adjacent(cube)) for cube in self.cubes])


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return [tuple(map(int, line.split(','))) for line in self.input]

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        return problem.solve()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
