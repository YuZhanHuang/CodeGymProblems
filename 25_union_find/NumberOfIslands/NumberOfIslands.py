# Number of Islands

class UnionFind:
    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # Function to find the root parent of a node
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Function to connect components
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    # Function to return the number of connected components consisting of "1"s
    def get_count(self):
        return self.count


def valid_direction(x, y, grid):
    n = len(grid)
    m = len(grid[0])
    if not (0 <= x <= n-1) or not (0 <= y <= m-1):
        return False
    if grid[x][y] == '1':
        return True
    return False


def num_islands(grid):
    uf = UnionFind(grid)
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] != "1":
                continue
            curr = (i, j)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            valid_moves = []
            for dir in directions:
                x = curr[0] + dir[0] 
                y = curr[1] + dir[1] 
                if valid_direction(x, y, grid):
                    valid_moves.append((x, y))
            curr_flatten = curr[0] * m + curr[1]
            for vm in valid_moves:
                vm_flatten = vm[0] * m + vm[1]
                uf.union(curr_flatten, vm_flatten)
        
    return uf.get_count()


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([["1", "1", "1", "1", "0"],
          ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]], 1),
        ([["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]], 3),
    ]
    
    print("Testing Number of Islands:")
    all_passed = True
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = num_islands(grid)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} num_islands(grid) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

