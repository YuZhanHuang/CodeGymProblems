# Largest Number After Digit Swaps by Parity

import heapq


def largest_integer(num):
    s = str(num)
    even_heap = []
    odd_heap = []
    locations = []  # even == 0, odd == 1 
    
    for c in s:
        val = int(c)
        if val % 2 == 0:
            heapq.heappush(even_heap, -val)
            locations.append(0)
        else:
            heapq.heappush(odd_heap, -val)
            locations.append(1)
    
    s = ''
    for location in locations:
        if location == 0:
            val = heapq.heappop(even_heap)
            val = -val
            s += str(val)
        else:
            val = heapq.heappop(odd_heap)
            val = -val
            s += str(val)
    
    return int(s)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (1234, 3412),
        (65875, 87655),
        (247, 427),
        (12, 12),  # 1 is odd, 2 is even, cannot swap
    ]
    
    print("Testing Largest Number After Digit Swaps by Parity:")
    all_passed = True
    for i, (num, expected) in enumerate(test_cases, 1):
        result = largest_integer(num)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} largest_integer({num}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

