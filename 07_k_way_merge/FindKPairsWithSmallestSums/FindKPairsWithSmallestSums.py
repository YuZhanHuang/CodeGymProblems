# Find K Pairs with Smallest Sums

from heapq import *


def k_smallest_pairs(list1, list2, k): 
    n, m = len(list1), len(list2)
    if n == 0 or m == 0 or k == 0:
        return []
    
    result = []
    heap = []
    
    for i in range(min(n, k)):
        heappush(heap, (list1[i] + list2[0], i, 0))
    
    while heap and len(result) < k:
        val, i, j = heappop(heap)
        result.append((list1[i], list2[j]))
        
        if j + 1 < m:
            heappush(heap, (list1[i] + list2[j+1], i, j+1))

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 7, 11], [2, 4, 6], 3, [(1, 2), (1, 4), (1, 6)]),
        ([1, 1, 2], [1, 2, 3], 2, [(1, 1), (1, 1)]),
        ([1, 2], [3], 3, [(1, 3), (2, 3)]),
    ]
    
    print("Testing Find K Pairs with Smallest Sums:")
    all_passed = True
    for i, (list1, list2, k, expected) in enumerate(test_cases, 1):
        result = k_smallest_pairs(list1, list2, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} k_smallest_pairs({list1}, {list2}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

