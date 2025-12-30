# Super Ugly Number

import heapq


def nth_super_ugly_number(n, primes):
    ugly = [1]
    min_heap = [(prime, prime, 0) for prime in primes]
    heapq.heapify(min_heap)

    while len(ugly) < n:
        next_ugly, prime, idx = heapq.heappop(min_heap)

        if next_ugly != ugly[-1]:
            ugly.append(next_ugly)

        heapq.heappush(min_heap, (prime * ugly[idx+1], prime, idx+1))

    return ugly[-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        (12, [2, 7, 13, 19], 32),
        (1, [2, 3, 5], 1),
        (10, [2, 3, 5], 12),
    ]
    
    print("Testing Super Ugly Number:")
    all_passed = True
    for i, (n, primes, expected) in enumerate(test_cases, 1):
        result = nth_super_ugly_number(n, primes)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} nth_super_ugly_number({n}, {primes}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

