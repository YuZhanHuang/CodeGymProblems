# Merge Intervals

def merge_intervals(intervals):
    result = [intervals[0][:]]
    for start, end in intervals[1:]:
        last_start, last_end = result[-1]
        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 4], [3, 6], [7, 9]], [[1, 6], [7, 9]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4]], [[1, 4]]),
        ([[1, 3], [2, 4], [3, 5], [6, 7]], [[1, 5], [6, 7]]),
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
        ([[1, 10], [2, 3], [4, 5], [6, 7]], [[1, 10]]),
    ]
    
    print("Testing Merge Intervals:")
    all_passed = True
    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = merge_intervals(intervals)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} merge_intervals({intervals}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

