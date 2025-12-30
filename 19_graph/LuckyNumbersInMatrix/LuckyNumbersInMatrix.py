# Lucky Numbers in a Matrix


def lucky_numbers(matrix):
    m, n = len(matrix), len(matrix[0])

    r_largest_min = float('-inf')
    for i in range(m):
        r_min = min(matrix[i])
        r_largest_min = max(r_largest_min, r_min)

    c_smallest_max = float("inf")
    for i in range(n):
        c_max = max(matrix[j][i] for j in range(m))
        c_smallest_max = min(c_smallest_max, c_max)

    return [r_largest_min] if r_largest_min == c_smallest_max else []


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
        ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
        ([[7, 8], [1, 2]], [7]),
    ]
    
    print("Testing Lucky Numbers in a Matrix:")
    all_passed = True
    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = lucky_numbers(matrix)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} lucky_numbers(...) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

