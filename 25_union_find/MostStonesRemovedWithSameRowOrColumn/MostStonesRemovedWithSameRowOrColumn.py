# Most Stones Removed with Same Row or Column

class UnionFind:
    # Constructor
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        
    # Function to find which group a particular element belongs.
    def find(self, coordinate):
        if coordinate != self.parents[coordinate]:
            self.parents[coordinate] = self.find(self.parents[coordinate])
        return self.parents[coordinate]

    # Function to join two coordinates into a single one.
    def union(self, x, y):
        # Set the parent of each node to itself 
        # if not already present in the dictionary
        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)

        # Set the ranks of each node to 0 
        # if not already present in the dictionary
        self.ranks.setdefault(x, 0)
        self.ranks.setdefault(y, 0)

        # Compare the ranks of the two nodes 
        # to decide which should be the parent
        if self.ranks[x] > self.ranks[y]:
            self.parents[self.find(y)] = self.find(x)
        elif self.ranks[y] > self.ranks[x]:
            self.parents[self.find(x)] = self.find(y)
        
        # If the ranks are equal, choose one node 
        # as the parent and increment its ranks
        else:
            self.parents[self.find(x)] = self.find(y)
            self.ranks[y] += 1


def remove_stones(stones):
    uf = UnionFind()
    n = len(stones)
    
    # 把所有石頭座標初始登記到 UF
    coords = [(x, y) for x, y in stones]
    for coord in coords:
        uf.parents.setdefault(coord, coord)
        uf.ranks.setdefault(coord, 0)
    
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i+1, n):
            x2, y2 = coords[j]
            if x1 == x2 or y1 == y2:
                uf.union((x1, y1), (x2, y2))
    
    roots = set()
    for coord in coords:
        roots.add(uf.find(coord))
    
    return n - len(roots)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
        ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
        ([[0, 0]], 0),
    ]
    
    print("Testing Most Stones Removed with Same Row or Column:")
    all_passed = True
    for i, (stones, expected) in enumerate(test_cases, 1):
        result = remove_stones(stones)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} remove_stones({stones}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

