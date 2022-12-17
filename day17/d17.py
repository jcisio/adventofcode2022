"""
Advent Of Code
--- Day 17: Pyroclastic Flow ---
https://adventofcode.com/2022/day/17
"""
class Problem:

    class Rock:
        def __init__(self, top, left) -> None:
            self.top = top
            self.left = left

    def __init__(self, input) -> None:
        self.pattern = input
        self.move = {'<': -1, '>': 1}
        self.rocks = [
            ['####'],
            [' # ','###',' # '],
            ['  #','  #','###'],
            ['#','#','#','#'],
            ['##','##']
        ]
        self.chamber = {}
        self.height = 0
        self.current_gas = 0
        self.current_rock = -1
        self.rock = None


    def drop_new_rock(self):
        self.current_rock = (self.current_rock + 1) % len(self.rocks)
        self.rock = Problem.Rock(self.height + len(self.rocks[self.current_rock]) + 3, 2)

    def can_move(self, top, left):
        #print(self.current_rock, self.rock.top, top, left)
        top = self.rock.top + top
        left = self.rock.left + left
        for j, line in enumerate(self.rocks[self.current_rock]):
            for i in range(len(line)):
                if line[i] == '#':
                    if left + i < 0 or left + i >= 7 or top - j <= 0 or (top - j, left + i) in self.chamber:
                        return False
        return True

    def move_one(self):
        if self.can_move(0, self.move[self.pattern[self.current_gas]]):
            self.rock.left += self.move[self.pattern[self.current_gas]]
        self.current_gas = (self.current_gas + 1) % len(self.pattern)
        if self.can_move(-1, 0):
            self.rock.top -= 1
            return True
        # If rock can't move down, then done.
        self.height = max(self.height, self.rock.top)
        for j, line in enumerate(self.rocks[self.current_rock]):
            for i in range(len(line)):
                if line[i] == '#':
                    self.chamber[(self.rock.top-j, self.rock.left+i)] = True
        return False

    def print(self):
        for j in range(self.height):
            print('|', end='')
            for i in range(7):
                print('#' if (self.height-j,i) in self.chamber else '.', end='')
            print('|')
        print('+-------+')

    def solve(self):
        c = 0
        while True:
            self.drop_new_rock()
            c += 1
            while self.move_one():
                pass
            if c == 2022:
                break
        #self.print()
        return self.height

    def solve2(self, rocks):
        delta = []
        height = []
        c = 0
        while True:
            self.drop_new_rock()
            c += 1
            while self.move_one():
                pass
            delta.append((self.current_rock, self.current_gas))
            height.append(self.height)
            # tortoise and hare algo
            if c > 2 and delta[-1] == delta[c//2]:
                break
        start = c // 2
        loop = c - 1 - start
        loop_height = height[start + loop] - height[start]
        return height[start] + (rocks - start)//loop*loop_height + height[(rocks - start) % loop + start] - height[start]


class Solver:
    def __init__(self, input) -> None:
        self.input = input
        pass

    def parse_input(self):
        return self.input[0]

    def solve(self, part=1):
        problem = Problem(self.parse_input())
        # Don't understand why -1
        return problem.solve() if part==1 else problem.solve2(1000000000000)-1


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
