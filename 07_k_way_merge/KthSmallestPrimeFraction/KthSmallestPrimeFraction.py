# Kth Smallest Prime Fraction

import heapq


def kth_smallest_prime_fraction(arr, k):
    n = len(arr)
    heap = []
    
    # Initialize heap with each numerator and the largest denominator
    for i in range(n - 1):
        heapq.heappush(heap, (arr[i] / arr[n-1], i, n-1))
    
    # Pop k-1 times to reach the k-th smallest
    for _ in range(k - 1):
        _, i, j = heapq.heappop(heap)
        # Move to the next smaller denominator for the same numerator
        if j - 1 > i:
            heapq.heappush(heap, (arr[i] / arr[j-1], i, j-1))
    
    # The k-th smallest fraction
    _, i, j = heapq.heappop(heap)
    
    return [arr[i], arr[j]]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 5], 3, [2, 5]),
        ([1, 7], 1, [1, 7]),
        ([1, 2, 3, 5, 7], 4, [1, 3]),  # Fractions: 1/7, 1/5, 2/7, 1/3, 2/5, ...
    ]
    
    print("Testing Kth Smallest Prime Fraction:")
    all_passed = True
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        result = kth_smallest_prime_fraction(arr, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} kth_smallest_prime_fraction({arr}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

