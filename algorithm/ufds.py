class UFDS:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.num_sets = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            i, j = j, i
        self.parent[j] = i
        self.size[i] += self.size[j]
        if self.rank[i] == self.rank[j]:
            self.rank[i] += 1
        self.num_sets -= 1

    def connected(self, i, j):
        return self.find(i) == self.find(j)