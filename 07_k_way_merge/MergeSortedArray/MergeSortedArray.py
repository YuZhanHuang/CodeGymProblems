# Merge Sorted Array

def merge_sorted(nums1, m, nums2, n):
    ptr = m + n - 1
    ptr1 = m - 1
    ptr2 = n - 1
    
    while ptr >= 0:
        if ptr2 < 0:
            break
        if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
            nums1[ptr] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[ptr] = nums2[ptr2]
            ptr2 -= 1
        
        ptr -= 1
    
    return nums1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]
    
    print("Testing Merge Sorted Array:")
    all_passed = True
    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases, 1):
        nums1_copy = nums1.copy()
        result = merge_sorted(nums1_copy, m, nums2, n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} merge_sorted({nums1}, {m}, {nums2}, {n}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

