# Jump Game I

def jump_game(nums):
    target_idx = len(nums) - 1

    for i in range(len(nums)-2, -1, -1):
        if target_idx <= i+nums[i]:
            target_idx = i

    return True if target_idx == 0 else False


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
    ]
    
    print("Testing Jump Game I:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = jump_game(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} jump_game({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

