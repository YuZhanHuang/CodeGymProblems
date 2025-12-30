# Kth Smallest Number in M Sorted Lists

from heapq import *


def k_smallest_number(lists, k):
    min_heap = []
    result = []
    
    for i in range(len(lists)):
        if lists[i]:
            heappush(min_heap, (lists[i][0], i, 0))
            
    if not min_heap:
        return 0
        
    while min_heap:
        ele, idx, idx2 = heappop(min_heap)
        
        if idx2 < len(lists[idx]) - 1:
            idx2 += 1
            heappush(min_heap, (lists[idx][idx2], idx, idx2))
        
        result.append(ele)
    
    return result[k-1] if k <= len(result) else result[-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5, 7),
        ([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 5, 5),
        ([[1, 2, 3]], 2, 2),
        ([], 1, 0),
        ([[1, 2, 3]], 10, 3),  # k > total elements
    ]
    
    print("Testing Kth Smallest Number in M Sorted Lists:")
    all_passed = True
    for i, (lists, k, expected) in enumerate(test_cases, 1):
        result = k_smallest_number(lists, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} k_smallest_number({lists}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

