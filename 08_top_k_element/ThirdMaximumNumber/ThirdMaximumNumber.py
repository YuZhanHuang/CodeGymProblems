# Third Maximum Number

from heapq import *


def third_max(nums): 
    counter = {}
    min_heap = []
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)
    
    for key, _ in counter.items():
        if len(min_heap) < 3:
            heappush(min_heap, key)
        else:
            if min_heap[0] < key:
                heappop(min_heap)
                heappush(min_heap, key)
                
    if len(min_heap) < 3:
        while len(min_heap) > 1:
            heappop(min_heap)
        return min_heap[0]
    
    return min_heap[0]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
    ]
    
    print("Testing Third Maximum Number:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = third_max(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} third_max({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

