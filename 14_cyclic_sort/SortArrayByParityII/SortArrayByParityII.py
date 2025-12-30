# Sort Array By Parity II

def sort_array_by_parityII(nums):
    even = 0
    odd = 1
    
    while even < len(nums) and odd < len(nums):
        if nums[even] % 2 == 0:
            even += 2
        elif nums[odd] % 2 == 1:
            odd += 2
        else:
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2
    
    return nums


# Helper function to check if array is valid
def is_valid(nums):
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 != 0:
            return False
        if i % 2 == 1 and nums[i] % 2 != 1:
            return False
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4, 2, 5, 7]),
        ([2, 3]),
        ([4, 1, 1, 0, 1, 0]),
    ]
    
    print("Testing Sort Array By Parity II:")
    all_passed = True
    for i, nums in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        result = sort_array_by_parityII(nums_copy)
        valid = is_valid(result)
        status = "✓" if valid else "✗"
        if not valid:
            all_passed = False
        print(f"Test {i}: {status} sort_array_by_parityII({nums}) = {result}, valid = {valid}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

