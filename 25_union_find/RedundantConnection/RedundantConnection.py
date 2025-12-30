# Redundant Connection

class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = [1] * (n + 1)
        for i in range(n + 1):
            self.parent.append(i)

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, v1, v2):
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] = self.rank[p1] + self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] = self.rank[p2] + self.rank[p1]
        
        return True


def redundant_connection(edges):
    nodes = len(edges)
    uf = UnionFind(nodes)
    result = []
    
    for u, v in edges:
        if not uf.union(u, v):
            result.append([u, v])
            break

    return result[0]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ]
    
    print("Testing Redundant Connection:")
    all_passed = True
    for i, (edges, expected) in enumerate(test_cases, 1):
        result = redundant_connection(edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} redundant_connection({edges}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

