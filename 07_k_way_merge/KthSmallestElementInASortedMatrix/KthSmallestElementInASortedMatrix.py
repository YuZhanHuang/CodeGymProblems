# Kth Smallest Element in a Sorted Matrix

from heapq import *


def kth_smallest_element(matrix, k):
    n = len(matrix)
    heap = []
    result = []
    
    for i in range(n):
        heappush(heap, (matrix[i][0], i, 0))
    
    while heap and len(result) < k:
        val, i, j = heappop(heap)
        result.append(val)
        
        if j + 1 < n:
            heappush(heap, (matrix[i][j+1], i, j+1))
    
    return result[-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[-5]], 1, -5),
        ([[1, 2], [1, 3]], 2, 1),
    ]
    
    print("Testing Kth Smallest Element in a Sorted Matrix:")
    all_passed = True
    for i, (matrix, k, expected) in enumerate(test_cases, 1):
        result = kth_smallest_element(matrix, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} kth_smallest_element(matrix, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

