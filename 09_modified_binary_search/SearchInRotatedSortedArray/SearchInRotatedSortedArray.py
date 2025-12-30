# Search in Rotated Sorted Array

def binary_search_rotated(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] <= nums[end]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ]
    
    print("Testing Search in Rotated Sorted Array:")
    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = binary_search_rotated(nums, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} binary_search_rotated({nums}, {target}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

