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
            s = self.sensors[i]
#            print(s[0], s[0]-s[4])

    @staticmethod
    def distance(sensor):
        return abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])

    def get_start_stop(self, n):
        l = []
#        print(f"--- Line {n} ---")
        for s in self.sensors:
#            print(f"sensor {s} distance {abs(s[1] - n)}")
            if abs(s[1] - n) <= s[4]:
                d = s[4] - abs(s[1] - n)
                l.append((s[0] - d, s[0] + d))
#                print(f'Position of this sensor: {s[0] - d}, {s[0] + d}')
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
        #print(self.sensors)
        for y in range(start, stop + 1):
            s = sorted(self.get_start_stop(y), key=lambda x:x[0])
            i = start
            for p in s:
                if p[1] <= i:
                    continue
                if p[0] > i+1:
                    print(i+1, y, s)
                    return y+(i+1)*stop
                if p[1] >= stop:
                    break
                i = p[1]
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        self.problem = None
        pass

    def parse_input(self):
        return [list(map(int, re.findall(r'-?\d+', x))) for x in self.input]

    def solve(self, part=1):
        self.problem = Problem(self.parse_input())
        y, m = (10, 20) if len(self.problem.sensors) < 20 else (2000000,4000000)
        if part==1:
            return self.problem.draw_line(y)
        else:
            return self.problem.find_bacon(0, m)


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
#print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
