# Find Right Interval

import heapq


def find_right_interval(intervals):
    result = [-1] * len(intervals)
    start_heap = []
    end_heap = []

    for idx, (start, end) in enumerate(intervals):
        heapq.heappush(start_heap, (start, idx))
        heapq.heappush(end_heap, (end, idx))
    
    while end_heap:
        end, idx = heapq.heappop(end_heap)
        
        while start_heap and start_heap[0][0] < end:
            heapq.heappop(start_heap)
            
        if start_heap:
            result[idx] = start_heap[0][1]
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 2]], [-1]),
        ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
        ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
    ]
    
    print("Testing Find Right Interval:")
    all_passed = True
    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = find_right_interval(intervals)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_right_interval({intervals}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

