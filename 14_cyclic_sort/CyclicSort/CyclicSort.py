# Cyclic Sort


def cyclic_sort(nums):
    idx = 0
    while idx < len(nums):
        correct = nums[idx] - 1
        if nums[idx] != nums[correct]:
            nums[idx], nums[correct] = nums[correct], nums[idx]
        else:
            idx += 1

    return nums


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 1, 5, 4, 2], [1, 2, 3, 4, 5]),
        ([2, 6, 4, 3, 1, 5], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 6, 4, 3, 2], [1, 2, 3, 4, 5, 6]),
    ]

    print("Testing Cyclic Sort:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        result = cyclic_sort(nums_copy)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} cyclic_sort({nums}) = {result}, expected {expected}")

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")
