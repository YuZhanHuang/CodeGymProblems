# Remove Covered Intervals

def remove_covered_intervals(intervals):
    # initialize
    intervals.sort(key=lambda x: (x[0], -x[1]))
    result = [intervals[0][:]]
    
    # main
    for interval in intervals[1:]:
        start, end = interval
        
        # is cover
        last_start, last_end = result[-1]
        if start >= last_start and end <= last_end:
            continue
        else:
            result.append([start, end])
            
    return len(result)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 4], [3, 6], [2, 8]], 2),
        ([[1, 4], [2, 3]], 1),
        ([[1, 2], [1, 4], [3, 4]], 1),
        ([[1, 4], [3, 6]], 2),
        ([[0, 10], [5, 12]], 2),
        ([[3, 10], [4, 10], [5, 11]], 2),
        ([[1, 4], [1, 2], [1, 3], [2, 4]], 1),
    ]
    
    print("Testing Remove Covered Intervals:")
    all_passed = True
    for i, (intervals, expected) in enumerate(test_cases, 1):
        # Make a copy to avoid mutation
        intervals_copy = [interval[:] for interval in intervals]
        result = remove_covered_intervals(intervals_copy)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} remove_covered_intervals({intervals}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

