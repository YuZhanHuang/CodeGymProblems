def circular_array_loop(nums):  
    size = len(nums)

    for i in range(size):
        slow = fast = i
        direction = nums[i] >= 0  # True -> False <- 

        while True:
            # slow move
            slow = next_step(nums, slow, size)
            if is_not_cycle(nums, direction, slow, size):
                break

            # fast move 1st
            fast = next_step(nums, fast, size)
            if is_not_cycle(nums, direction, fast, size):
                break

            # fast move 2nd
            fast = next_step(nums, fast, size)
            if is_not_cycle(nums, direction, fast, size):
                break
            
            if slow == fast:
                return True
    
    return False


def next_step(nums, pointer, size):
    return (pointer + nums[pointer]) % size


def is_not_cycle(nums, pre_direction, pointer, size):
    cur_direction = nums[pointer] >= 0

    if pre_direction != cur_direction or abs(nums[pointer]) % size == 0:
        return True

    return False


def main():
    """Test cases for Circular Array Loop"""
    test_cases = [
        # (nums, expected_output, description)
        ([2, -1, 1, 2, 2], True, "Valid cycle in forward direction"),
        ([-1, 2], False, "Changes direction, no valid cycle"),
        ([-2, 1, -1, -2, -2], False, "No cycle in single direction"),
        ([1, 1, 1, 1, 1], True, "All forward, creates cycle"),
        ([-1, -2, -3, -4, -5], False, "All backward but no cycle"),
    ]
    
    print("=" * 70)
    print("Testing: Circular Array Loop")
    print("=" * 70)
    
    all_passed = True
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = circular_array_loop(nums.copy())
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

