f = open(__file__[:-3] + '.in', 'r')


class Monkey:
    def __init__(self, items, op1, op2, test, target1, target2):
        self.items = items
        self.op = (op1, op2)
        self.test = test
        self.targets = (target1, target2)
        self.inspections = 0

    def do_op(self, level):
        if self.op[0] == '+':
            level = level + self.op[1]
        elif self.op[0] == '*':
            level = level * (self.op[1] if self.op[1] > 0 else level)
        return level//3

    def inspect(self):
        targets = []
        self.inspections += len(self.items)
        while self.items:
            level = self.items.pop(0)
            level = self.do_op(level)
            target = self.targets[0 if level % self.test == 0 else 1]
            targets.append((level, target))
        return targets

    def __str__(self):
        return f"Items {self.items} Ops {self.op} Test {self.test} Targets {self.targets} INS {self.inspections}"


def do_round(monkeys):
    for m in monkeys:
        targets = m.inspect()
        for t in targets:
            monkeys[t[1]].items.append(t[0])
#    for m in monkeys:
#        print(m)


def parse_data(lines):
    monkeys = []
    while lines:
        lines.pop(0)
        items = list(map(int, lines.pop(0).split(': ')[1].split(', ')))
        ops = lines.pop(0).split()
        op1 = ops[-2]
        op2 = 0 if ops[-1] == 'old' else int(ops[-1])
        test = int(lines.pop(0).split()[-1])
        target1 = int(lines.pop(0).split()[-1])
        target2 = int(lines.pop(0).split()[-1])
        monkeys.append(Monkey(items, op1, op2, test, target1, target2))
        if lines: lines.pop(0)
    return monkeys


def solve(monkeys):
    for _ in range(20):
        do_round(monkeys)
    inspections = sorted(map(lambda x: x.inspections, monkeys))
    return inspections[-1]*inspections[-2]


lines = f.read().strip().split('\n')
monkeys = parse_data(lines)
print("Puzzle 1: ", solve(monkeys))
