# Insert Interval

def insert_interval(intervals, new_interval):
    new_start, new_end = new_interval
    output = []
    inserted = False

    for cur_start, cur_end in intervals:
        if cur_end < new_start:
            # this interval is completely before new_interval
            output.append([cur_start, cur_end])

        elif cur_start > new_end:
            # this interval is completely after new_interval—
            # if we haven't yet inserted new_interval, do it now:
            if not inserted:
                output.append([new_start, new_end])
                inserted = True
            output.append([cur_start, cur_end])

        else:
            # overlapping: extend the new_interval to cover it
            new_start = min(new_start, cur_start)
            new_end   = max(new_end,   cur_end)

    # if new_interval goes at the very end
    if not inserted:
        output.append([new_start, new_end])

    return output


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        ([[1, 5]], [0, 0], [[0, 0], [1, 5]]),
        ([[3, 5], [8, 10]], [1, 2], [[1, 2], [3, 5], [8, 10]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ]
    
    print("Testing Insert Interval:")
    all_passed = True
    for i, (intervals, new_interval, expected) in enumerate(test_cases, 1):
        result = insert_interval(intervals, new_interval)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status}")
        if result != expected:
            print(f"  Input:    {intervals}, new={new_interval}")
            print(f"  Output:   {result}")
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

