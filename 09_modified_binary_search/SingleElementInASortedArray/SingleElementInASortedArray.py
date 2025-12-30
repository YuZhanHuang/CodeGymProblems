# Single Element in a Sorted Array

def single_non_duplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        # 保證 mid 是偶數，對齊到「每對的第一個元素」
        if mid % 2 == 1:
            mid -= 1
        
        if nums[mid] == nums[mid + 1]:
            # 這是一對，唯一元素在右邊
            left = mid + 2
        else:
            # 這對被打散了，唯一元素在左邊（包含 mid）
            right = mid
    
    # 收斂到同一個位置，就是答案
    return nums[left]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1], 1),
    ]
    
    print("Testing Single Element in a Sorted Array:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = single_non_duplicate(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} single_non_duplicate({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

