f = open(__file__[:-3] + '.in', 'r')


class Waterfall:
    source = (500,0)
    def __init__(self) -> None:
        self.rock = dict()
        self._depth = None

    @property
    def depth(self) -> int:
        if self._depth is None:
            self._depth = max([r[1] for r in self.rock])
        return self._depth

    def add_rocks(self, a, b):
        if a[0] == b[0]:
            for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                self.rock[(a[0], i)] = '#'
        elif a[1] == b[1]:
            for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                self.rock[(i, a[1])] = '#'
        # Unset depth to recompute
        self._depth = None

    def add_floor(self):
        d = self.depth + 2
        self.add_rocks((self.source[0] - d - 2, d), (self.source[0] + d + 2, d))

    # Drop a sand. Return True if it is not blocked or not leaked.
    def drop_sand(self) -> bool:
        a = self.source
        while a[1] <= self.depth:
            if (a[0], a[1] + 1) not in self.rock:
                a = (a[0], a[1] + 1)
            elif (a[0] - 1, a[1] + 1) not in self.rock:
                a = (a[0] - 1, a[1] + 1)
            elif (a[0] + 1, a[1] + 1) not in self.rock:
                a = (a[0] + 1, a[1] + 1)
            elif a not in self.rock:
                self.rock[a] = 'o'
                break
            else:
                return False
#        print(a)
        return a[1] < self.depth


def parse_input(lines) -> Waterfall:
    waterfall = Waterfall()
    for line in lines:
        points = list(map(lambda x: list(map(int, x.split(','))), line.split(' -> ')))
        for i in range(len(points)-1):
            waterfall.add_rocks(points[i], points[i+1])
    return waterfall


def solve(lines, part=1):
    waterfall = parse_input(lines)
    if part==2:
        waterfall.add_floor()
    c = 0
    while waterfall.drop_sand():
        c += 1
    return c


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solve(lines))
print("Puzzle 2: ", solve(lines, 2))
