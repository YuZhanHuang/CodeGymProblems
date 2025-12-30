# Generate Parentheses

def backtracking(n, left_count, right_count, output, result):
    if left_count >= n and right_count >= n:
        result.append(''.join(output))

        return

    if left_count < n:
        output.append('(')    
        backtracking(n, left_count+1, right_count, output, result)
        output.pop()
    
    if right_count < left_count:
        output.append(')')
        backtracking(n, left_count, right_count+1, output, result)
        output.pop()


def generate_combinations(n):
    result = []
    output = []
    left_count, right_count = 0, 0
    backtracking(n, left_count, right_count, output, result)

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
    ]
    
    print("Testing Generate Parentheses:")
    all_passed = True
    for i, (n, expected) in enumerate(test_cases, 1):
        result = generate_combinations(n)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} generate_combinations({n}) = {result}")
        if result_sorted != expected_sorted:
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

