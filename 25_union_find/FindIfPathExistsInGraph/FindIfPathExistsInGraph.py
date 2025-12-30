# Find if Path Exists in Graph

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y


def valid_path(n, edges, source, destination):
    # source and destination is connected component
    uf = UnionFind(n)
    
    for u, v in edges:
        uf.union(u, v)
    
    src_root = uf.find(source)
    dest_root = uf.find(destination)
  
    return True if src_root == dest_root else False


# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    ]
    
    print("Testing Find if Path Exists in Graph:")
    all_passed = True
    for i, (n, edges, source, destination, expected) in enumerate(test_cases, 1):
        result = valid_path(n, edges, source, destination)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} valid_path(n={n}, source={source}, dest={destination}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

