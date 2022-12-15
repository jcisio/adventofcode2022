"""
Advent Of Code
--- Day 15: Beacon Exclusion Zone ---
https://adventofcode.com/2022/day/15
"""
import functools
import re


class Problem:
    def __init__(self, sensors) -> None:
        self.sensors = sensors
        for i in range(len(self.sensors)):
            self.sensors[i].append(self.distance(self.sensors[i]))

    @staticmethod
    def distance(sensor):
        return abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])

    def get_start_stop(self, n):
        l = []
        for s in self.sensors:
            print(s)
            if abs(s[1] - n) <= s[4]:
                d = s[4] - abs(s[1] - n)
                l.append((s[0] - d, s[0] + d))
        return l


    def draw_line(self, n):
        m = set()
        b = set()
        for s in self.sensors:
            if s[3] == n:
                b.add(s[2])
            if abs(s[1] - n) < s[4]:
                d = s[4] - abs(s[1] - n)
                for i in range(s[0] - d, s[0] + d + 1):
                    m.add(i)
        #print(m, b)
        return len(m) - len(b)

    def find_bacon(self, start, stop):
        print(self.sensors)
        for y in range(start, stop + 1):
            s = sorted(self.get_start_stop(y), key=lambda x:x[0])
            i = start
            for p in s:
                if p[1] < i:
                    continue
                if p[0] > i:
                    print(y, s)
                    return y
                if p[1] > stop:
                    break
                i = p[1]
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        self.problem = None
        pass

    def parse_input(self):
        return [list(map(int, re.findall(r'\d+', x))) for x in self.input]

    def solve(self, part=1):
        self.problem = Problem(self.parse_input())
        if part==1:
            return self.problem.draw_line(2000000)
        else:
            return self.problem.find_bacon(0, 4000000)


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
#print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
