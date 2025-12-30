# Kth Largest Element in an Array

import heapq


def find_kth_largest(nums, k):
    # 維持大小為k的 min heap
    kth_largest = []
    for num in nums:
        if len(kth_largest) < k:
            heapq.heappush(kth_largest, num)
        elif kth_largest[0] < num:
            heapq.heappop(kth_largest)
            heapq.heappush(kth_largest, num)

    return kth_largest[0]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
    ]
    
    print("Testing Kth Largest Element in an Array:")
    all_passed = True
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = find_kth_largest(nums, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_kth_largest({nums}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

