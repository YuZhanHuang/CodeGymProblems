# Flood Fill

def search_dfs(origin, sr, sc, grid, target):
    # base case
    if sr < 0 or sc < 0 or sr > len(grid) - 1 or sc > len(grid[sr]) - 1:
        return 

    # grid[sr][sc] == target 碰到起點
    if grid[sr][sc] != origin:
        return
    
    grid[sr][sc] = target

    for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        search_dfs(origin, sr+row_offset, sc+col_offset, grid, target)


def flood_fill(grid, sr, sc, target):
    if not grid:
        return []

    if grid[sr][sc] == target:
        return grid

    origin = grid[sr][sc]
    search_dfs(origin, sr, sc, grid, target)

    return grid


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
    ]
    
    print("Testing Flood Fill:")
    all_passed = True
    for i, (grid, sr, sc, target, expected) in enumerate(test_cases, 1):
        grid_copy = [row[:] for row in grid]
        result = flood_fill(grid_copy, sr, sc, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} flood_fill(grid, sr={sr}, sc={sc}, target={target})")
        print(f"  Result: {result}")
        if result != expected:
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

