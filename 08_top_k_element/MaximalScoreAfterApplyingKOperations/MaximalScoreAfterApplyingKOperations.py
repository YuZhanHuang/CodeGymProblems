# Maximal Score After Applying K Operations

import heapq
import math


def max_score(nums, k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
    
    total = 0
    while k > 0:
        num = heapq.heappop(max_heap)
        total += -num
        num = math.ceil(-num / 3)
    
        heapq.heappush(max_heap, -num)
        k -= 1
    
    return total


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([10, 10, 10, 10, 10], 5, 50),
        ([1, 10, 3, 3, 3], 3, 17),
    ]
    
    print("Testing Maximal Score After Applying K Operations:")
    all_passed = True
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = max_score(nums, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} max_score({nums}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

