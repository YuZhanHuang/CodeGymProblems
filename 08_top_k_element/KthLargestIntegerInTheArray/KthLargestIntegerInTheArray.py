# Kth Largest Integer in the Array

import heapq


def kth_largest_integer(nums, k): 
    nums = [int(num) for num in nums]
    min_heap = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
    
    return str(min_heap[0])


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["3", "6", "7", "10"], 4, "3"),
        (["2", "21", "12", "1"], 3, "2"),
        (["0", "0"], 2, "0"),
    ]
    
    print("Testing Kth Largest Integer in the Array:")
    all_passed = True
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = kth_largest_integer(nums, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} kth_largest_integer({nums}, {k}) = '{result}', expected '{expected}'")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

