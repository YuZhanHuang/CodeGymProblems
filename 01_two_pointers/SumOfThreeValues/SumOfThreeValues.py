# Sum of Three Values

def find_sum_of_three(nums, target):
   nums.sort()
   for i in range(len(nums)):
      low = i + 1
      high = len(nums) - 1

      while low < high:
         if target == nums[i] + nums[low] + nums[high]:
            return True
         elif target < nums[i] + nums[low] + nums[high]:
            high -= 1
         else:
            low += 1

   return False


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, -1, 0], 0, True),
        ([3, 7, 1, 2, 8, 4, 5], 10, True),
        ([3, 7, 1, 2, 8, 4, 5], 21, False),
        ([-1, 2, 1, -4, 5, -3], -8, True),
        ([-1, 2, 1, -4, 5, -3], 0, True),  # Fixed: -4 + -1 + 5 = 0
        ([1, 2, 3], 6, True),
        ([1, 2, 3], 10, False),
        ([0, 0, 0], 0, True),
        ([1, 1, 1], 3, True),
        ([1, 1, 1], 4, False),
    ]
    
    print("Testing Sum of Three Values:")
    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = find_sum_of_three(nums, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_sum_of_three({nums}, {target}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

