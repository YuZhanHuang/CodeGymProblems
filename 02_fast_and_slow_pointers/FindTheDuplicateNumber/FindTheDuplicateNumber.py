def find_duplicate(nums):
    fast = slow = nums[0]
  
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
   
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast


def main():
    """Test cases for Find The Duplicate Number"""
    test_cases = [
        # (nums, expected_duplicate, description)
        ([1, 3, 4, 2, 2], 2, "Duplicate is 2"),
        ([3, 1, 3, 4, 2], 3, "Duplicate is 3"),
        ([1, 1], 1, "Only two elements, duplicate is 1"),
        ([1, 1, 2], 1, "Duplicate is 1 in small array"),
        ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1, 4], 9, "Duplicate is 9 in larger array"),
    ]
    
    print("=" * 70)
    print("Testing: Find The Duplicate Number")
    print("=" * 70)
    
    all_passed = True
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = find_duplicate(nums.copy())
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Description: {description}")
    
    print("\n" + "=" * 70)
    if all_passed:
        print("All tests PASSED! ✓")
    else:
        print("Some tests FAILED! ✗")
    print("=" * 70)
    
    return all_passed


if __name__ == "__main__":
    main()

