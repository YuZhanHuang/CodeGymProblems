# Word Search

def dfs(row, col, idx, word, grid):
    if len(word) == idx:
        return True
        
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != word[idx]:
        return False
    
    temp = grid[row][col]
    grid[row][col] = '*'
    
    for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if dfs(row+row_offset, col+col_offset, idx+1, word, grid):
            return True
    
    grid[row][col] = temp
    
    return False


def word_search(grid, word):
    m = len(grid)
    n = len(grid[0])
    
    for row in range(m):
        for col in range(n):
            if dfs(row, col, 0, word, grid):
                return True

    return False


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
    ]
    
    print("Testing Word Search:")
    all_passed = True
    for i, (grid, word, expected) in enumerate(test_cases, 1):
        # Make a copy of grid for each test
        grid_copy = [row[:] for row in grid]
        result = word_search(grid_copy, word)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} word_search(grid, '{word}') = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

