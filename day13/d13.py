f = open(__file__[:-3] + '.in', 'r')


class Packet(list):
    @staticmethod
    def from_string(packet_string: str):
        packet = eval(packet_string)
        return Packet(packet)

    def __lt__(self, other):
#        print("Comparing", self, other)
        for i, item in enumerate(self):
            if i == len(other):
                return False
            op = other[i]
            if isinstance(item, int) and isinstance(op, int):
                if item < op:
                    return True
                if item > op:
                    return False
            else:
                p1 = Packet(item if isinstance(item, list) else [item])
                p2 = Packet(op if isinstance(op, list) else [op])
                if p1 < p2:
                    return True
                elif p2 < p1:
                    return False
        return True if len(self) < len(other) else False

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i, item in enumerate(self):
            op = other[i]
            if isinstance(item, int) and isinstance(op, int):
                if item != op:
                    return False
            else:
                p1 = Packet(item if isinstance(item, list) else [item])
                p2 = Packet(op if isinstance(op, list) else [op])
                if p1 == p2:
                    continue
                return False
        return True


def solve(lines):
    i = 1
    s = 0
    while len(lines) > 2:
        p1 = Packet(eval(lines.pop(0)))
        p2 = Packet(eval(lines.pop(0)))
        lines.pop(0)
        if p1 < p2:
            s += i
        i += 1
    return s


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solve(lines))
