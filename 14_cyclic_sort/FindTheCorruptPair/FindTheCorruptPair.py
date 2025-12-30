# Find the Corrupt Pair

def find_corrupt_pair(nums):
    # initialize variable 
    idx = 0
    missing = None
    duplicate = None
    
    while idx < len(nums):
        correct = nums[idx] - 1
        # swap element
        if nums[correct] != nums[idx]:
            nums[idx], nums[correct] = nums[correct], nums[idx]
        else:
            idx += 1
    
    for i in range(len(nums)):
        if nums[i] - 1 != i:
            missing = i + 1
            duplicate = nums[i]
    
    return [missing, duplicate]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 4], [3, 2]),
        ([1, 3, 3], [2, 3]),
        ([2, 2], [1, 2]),
    ]
    
    print("Testing Find the Corrupt Pair:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        result = find_corrupt_pair(nums_copy)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_corrupt_pair({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

