# Count Days Without Meetings

def count_days(days, meetings):
    # initialize variable
    meetings.sort(key=lambda x: x[0])
    total = 0
    
    # allowed interval
    result = [meetings[0][:]]  
    
    # main
    # merge interval
    for i in range(1, len(meetings)):
        start2, end2 = meetings[i]
        if start2 <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end2)
        else:
            result.append([start2, end2])
            
    # count total
    total = sum(end - start + 1 for start, end in result)
    
    return days - total


# Test cases
if __name__ == "__main__":
    test_cases = [
        (10, [[5, 7], [1, 3], [9, 10]], 2),
        (5, [[2, 4], [1, 3]], 1),
        (6, [[1, 6]], 0),
        (8, [[1, 2], [4, 5], [7, 8]], 2),  # Free days: 3, 6
        (10, [[1, 3], [5, 7], [9, 10]], 2),  # Free days: 4, 8
        (20, [[1, 5], [6, 10], [11, 15]], 5),
    ]
    
    print("Testing Count Days Without Meetings:")
    all_passed = True
    for i, (days, meetings, expected) in enumerate(test_cases, 1):
        # Make a copy to avoid mutation
        meetings_copy = [m[:] for m in meetings]
        result = count_days(days, meetings_copy)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} count_days({days}, {meetings}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

