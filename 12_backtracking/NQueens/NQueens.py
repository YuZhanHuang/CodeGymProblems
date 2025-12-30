# N-Queens

def is_valid_move(possible_row, possible_col, solution):
    for old_row in range(possible_row):
        old_col = solution[old_row]
        # 同列衝突
        if possible_col == old_col:
            return False
        # 同對角線衝突：行差 = 列差
        if abs(possible_row - old_row) == abs(possible_col - old_col):
            return False
    return True


def solve_n_queens_recursive(n, solution, row, result):
    if row == n:
        result.append(solution[:])
        return
  
    for i in range(n):
        if is_valid_move(row, i, solution):
            solution[row] = i
            solve_n_queens_recursive(n, solution, row+1, result)
            solution[row] = -1


def solve_n_queens(n):
    result = []
    solution = [-1] * n
    solve_n_queens_recursive(n, solution, 0, result)

    return len(result)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (4, 2),
        (1, 1),
        (8, 92),
    ]
    
    print("Testing N-Queens:")
    all_passed = True
    for i, (n, expected) in enumerate(test_cases, 1):
        result = solve_n_queens(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} solve_n_queens({n}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

