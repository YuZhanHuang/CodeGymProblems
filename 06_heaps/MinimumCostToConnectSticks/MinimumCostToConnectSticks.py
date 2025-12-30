# Minimum Cost to Connect Sticks

import heapq


def connect_sticks(sticks):
    heapq.heapify(sticks)
    costs = 0
    
    while sticks:
        if len(sticks) == 1:
            break
        
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        costs += (first + second)
        
        heapq.heappush(sticks, first + second)
    
    return costs


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 4, 3], 14),
        ([1, 8, 3, 5], 30),
        ([5], 0),
        ([1, 2], 3),
    ]
    
    print("Testing Minimum Cost to Connect Sticks:")
    all_passed = True
    for i, (sticks, expected) in enumerate(test_cases, 1):
        result = connect_sticks(sticks.copy())
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} connect_sticks({sticks}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

