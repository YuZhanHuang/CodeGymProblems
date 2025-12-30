# K Closest Points to Origin

from heapq import *


def k_closest(points, k):
    max_heap = []
    for i in range(k):
        x, y = points[i]
        dis = x**2 + y**2
        heappush(max_heap, (-dis, points[i]))
    
    for j in range(k, len(points)):
        x, y = points[j]
        dis = x**2 + y**2
        if -max_heap[0][0] > dis:
            heappop(max_heap)
            heappush(max_heap, (-dis, points[j]))
    
    return [point for _, point in max_heap]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ]
    
    print("Testing K Closest Points to Origin:")
    all_passed = True
    for i, (points, k, expected) in enumerate(test_cases, 1):
        result = k_closest(points, k)
        # Sort both result and expected for comparison
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} k_closest({points}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

