# Frequency of the Most Frequent Element


def max_frequency(nums, k):
    nums.sort()
    n = len(nums)
    start = 0
    max_freq = 1

    # 紀錄當前窗口 nums[start..end] 的總和
    window_sum = 0

    for end in range(n):
        # 新增右端元素到窗口總和
        window_sum += nums[end]

        # 計算：若要把整個窗口拉成 nums[end]，需要的 +1 操作數
        # target * window_len − window_sum
        # window_len == end−start+1
        required_ops = nums[end] * (end - start + 1) - window_sum

        # 當所需操作超過 k 時，就一直收縮左邊界
        while required_ops > k:
            # 把最左邊元素踢出窗口總和
            window_sum -= nums[start]
            start += 1

            # 重新計算這個新窗口的需求
            required_ops = nums[end] * (end - start + 1) - window_sum

        # 此時 [start..end] 是合法窗口，更新答案
        max_freq = max(max_freq, end - start + 1)

    return max_freq


# Driver code
def main():
    # Test case 1: Basic case
    nums1 = [1, 2, 4]
    k1 = 5
    result1 = max_frequency(nums1, k1)
    expected1 = 3  # [1,2,4] -> [4,4,4] requires 3+2=5 operations
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: Already same elements
    nums2 = [1, 4, 8, 13]
    k2 = 5
    result2 = max_frequency(nums2, k2)
    expected2 = 2  # [4,8] -> [8,8] requires 4 operations, or [8,13] -> [13,13] requires 5 operations
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: All elements can be made equal
    nums3 = [3, 9, 6]
    k3 = 2
    result3 = max_frequency(nums3, k3)
    expected3 = 1  # Can't make 2 elements equal with k=2
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Large k value
    nums4 = [1, 1, 1, 2, 2, 4]
    k4 = 10
    result4 = max_frequency(nums4, k4)
    expected4 = 5  # [1,1,2,2,4] -> [4,4,4,4,4] requires exactly 10 operations
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Single element
    nums5 = [5]
    k5 = 10
    result5 = max_frequency(nums5, k5)
    expected5 = 1  # Only one element
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
