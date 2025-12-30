# First Missing Positive

def smallest_missing_positive_integer(nums):
    i = 0
    while i < len(nums):
        correct_spot = nums[i] - 1
        if 0 <= correct_spot < len(nums) and nums[i] != nums[correct_spot]:
            nums[i], nums[correct_spot] = nums[correct_spot], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1
    return len(nums) + 1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
    ]
    
    print("Testing First Missing Positive:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        result = smallest_missing_positive_integer(nums_copy)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} smallest_missing_positive_integer({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

