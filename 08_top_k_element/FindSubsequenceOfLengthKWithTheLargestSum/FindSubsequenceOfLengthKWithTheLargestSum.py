# Find Subsequence of Length K with the Largest Sum

from heapq import *


def max_subsequence(nums, k):
    min_heap = []
    
    for i in range(k):
        heappush(min_heap, nums[i])
        
    for j in range(k, len(nums)):
        if min_heap[0] < nums[j]:
            heappop(min_heap)
            heappush(min_heap, nums[j])
    
    return sorted(min_heap, reverse=True)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 3], 2, [3, 3]),
        ([-1, -2, 3, 4], 3, [4, 3, -1]),
        ([3, 4, 3, 3], 2, [4, 3]),
    ]
    
    print("Testing Find Subsequence of Length K with the Largest Sum:")
    all_passed = True
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = max_subsequence(nums, k)
        result_sorted = sorted(result, reverse=True)
        expected_sorted = sorted(expected, reverse=True)
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} max_subsequence({nums}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

