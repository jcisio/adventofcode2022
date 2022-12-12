f = open(__file__[:-3] + '.in', 'r')


class Problem:
    def __init__(self, lines) -> None:
        self.M = len(lines)
        self.N = len(lines[0])
        self.nodes = dict()
        self.next = dict()
        self.dist = dict()
        for m in range(self.M):
            for n in range(self.N):
                self.nodes[(m, n)] = lines[m][n]
                if lines[m][n] == 'S':
                    self.start = (m, n)
                elif lines[m][n] == 'E':
                    self.end = (m, n)
        for n in self.nodes:
            self.next[n] = []
            self.dist[n] = self.M * self.N
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if self.accessible(n, (n[0] + d[0], n[1] + d[1])):
                    self.next[n].append((n[0] + d[0], n[1] + d[1]))

    def accessible(self, a, b) -> bool:
        if b not in self.nodes:
            return False
        a = 'a' if self.nodes[a] == 'S' else 'z' if self.nodes[a] == 'E' else self.nodes[a]
        b = 'a' if self.nodes[b] == 'S' else 'z' if self.nodes[b] == 'E' else self.nodes[b]
        return ord(b) - ord(a) <= 1

    def findMin(self, visited):
        min = self.M * self.N + 1
        for n in self.nodes:
            if self.dist[n] < min and n not in visited:
                min = self.dist[n]
                min_index = n
        return min_index

    def solve(self):
        visited = set()
        self.dist[self.start] = 0
        for _ in range(self.M * self.N):
            a = self.findMin(visited)
            visited.add(a)
            for b in self.next[a]:
                if b not in visited and self.dist[b] > self.dist[a] + 1:
                    self.dist[b] = self.dist[a] + 1
        return self.dist[self.end]


lines = f.read().strip().split('\n')
p = Problem(lines)
print("Puzzle 1: ", p.solve())
