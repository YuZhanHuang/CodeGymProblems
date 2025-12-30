# Count Pairs Whose Sum is Less than Target

def count_pairs(nums, target):
    nums.sort()
    count = 0
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            # All pairs (left, left+1), (left, left+2), …, (left, right)
            # have sum < target, so add them all at once:
            count += (right - left)
            left += 1
        else:
            # Sum is too big, shrink from the right
            right -= 1

    return count


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-1, 1, 2, 3, 1], 2, 3),
        ([-6, 2, 5, -2, -7, -1, 3], -2, 10),
        ([1, 2, 3, 4], 5, 2),
        ([1, 1, 1, 1], 3, 6),
        ([5, 4, 3, 2, 1], 10, 10),
        ([1, 2], 3, 0),  # 1+2=3, not < 3
        ([1, 2], 4, 1),
        ([1], 0, 0),
    ]
    
    print("Testing Count Pairs Whose Sum is Less than Target:")
    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = count_pairs(nums.copy(), target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} count_pairs({nums}, {target}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

