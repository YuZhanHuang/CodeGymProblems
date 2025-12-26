# Minimum Size Subarray Sum


def min_sub_array_len(target: int, nums: list[int]) -> int:
    n = len(nums)
    left = 0  # 左指針
    window_sum = 0  # 紀錄目前窗口的總和
    min_length = float("inf")  # 初始化最小長度為無限大

    # 右指針不斷往右擴展窗口
    for right in range(n):
        window_sum += nums[right]  # 將右指針的元素加入總和

        # 當窗口總和 ≥ target 時，嘗試縮小窗口
        while window_sum >= target:
            # 更新最小長度
            if right - left + 1 < min_length:
                min_length = right - left + 1

            # 縮小窗口，移動左指針
            window_sum -= nums[left]
            left += 1

    # 如果找不到符合條件的子陣列，返回 0
    return min_length if min_length != float("inf") else 0


# Driver code
def main():
    # Test case 1: Basic case
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    result1 = min_sub_array_len(target1, nums1)
    expected1 = 2  # [4,3]
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: No valid subarray
    target2 = 11
    nums2 = [1, 1, 1, 1, 1, 1, 1, 1]
    result2 = min_sub_array_len(target2, nums2)
    expected2 = 0  # Can't reach target
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: Single element sufficient
    target3 = 4
    nums3 = [1, 4, 4]
    result3 = min_sub_array_len(target3, nums3)
    expected3 = 1  # [4]
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Entire array needed
    target4 = 15
    nums4 = [1, 2, 3, 4, 5]
    result4 = min_sub_array_len(target4, nums4)
    expected4 = 5  # [1,2,3,4,5]
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Large target with small numbers
    target5 = 213
    nums5 = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    result5 = min_sub_array_len(target5, nums5)
    expected5 = 8  # [83,4,25,26,25,2,25,25]
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
