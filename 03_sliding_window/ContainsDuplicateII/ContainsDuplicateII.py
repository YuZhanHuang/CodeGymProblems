def contains_nearby_duplicate(nums, k):
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            return True

        seen.add(nums[i])

        if len(seen) > k:
            seen.remove(nums[i - k])

    return False


# Driver code
def main():
    # Test case 1: 基本测试 - 有重复元素且距离 <= k
    nums1 = [1, 2, 3, 1]
    k1 = 3
    result1 = contains_nearby_duplicate(nums1, k1)
    print(f"Test case 1: nums = {nums1}, k = {k1}")
    print(f"Expected: True (索引 0 和 3 的元素相同，距离为 3 <= 3)")
    print(f"Result: {result1}")
    print(f"Pass: {result1 == True}\n")

    # Test case 2: 有重复元素但距离 > k
    nums2 = [1, 0, 1, 1]
    k2 = 1
    result2 = contains_nearby_duplicate(nums2, k2)
    print(f"Test case 2: nums = {nums2}, k = {k2}")
    print(f"Expected: True (索引 2 和 3 的元素相同，距离为 1 <= 1)")
    print(f"Result: {result2}")
    print(f"Pass: {result2 == True}\n")

    # Test case 3: 没有重复元素
    nums3 = [1, 2, 3, 4, 5]
    k3 = 3
    result3 = contains_nearby_duplicate(nums3, k3)
    print(f"Test case 3: nums = {nums3}, k = {k3}")
    print(f"Expected: False (没有重复元素)")
    print(f"Result: {result3}")
    print(f"Pass: {result3 == False}\n")

    # Test case 4: 边界情况 - k = 0
    nums4 = [1, 2, 3, 1]
    k4 = 0
    result4 = contains_nearby_duplicate(nums4, k4)
    print(f"Test case 4: nums = {nums4}, k = {k4}")
    print(f"Expected: False (k = 0 表示没有两个不同的索引满足条件)")
    print(f"Result: {result4}")
    print(f"Pass: {result4 == False}\n")

    # Test case 5: 边界情况 - 数组长度为 1
    nums5 = [1]
    k5 = 1
    result5 = contains_nearby_duplicate(nums5, k5)
    print(f"Test case 5: nums = {nums5}, k = {k5}")
    print(f"Expected: False (只有一个元素，无法找到两个不同的索引)")
    print(f"Result: {result5}")
    print(f"Pass: {result5 == False}\n")

    # Test case 6: 相邻重复元素，k = 1
    nums6 = [1, 1]
    k6 = 1
    result6 = contains_nearby_duplicate(nums6, k6)
    print(f"Test case 6: nums = {nums6}, k = {k6}")
    print(f"Expected: True (索引 0 和 1 的元素相同，距离为 1 <= 1)")
    print(f"Result: {result6}")
    print(f"Pass: {result6 == True}\n")

    # Test case 7: 多个重复元素的情况
    nums7 = [1, 2, 3, 1, 2, 3]
    k7 = 2
    result7 = contains_nearby_duplicate(nums7, k7)
    print(f"Test case 7: nums = {nums7}, k = {k7}")
    print(f"Expected: False (重复元素之间的距离都 > 2)")
    print(f"Result: {result7}")
    print(f"Pass: {result7 == False}\n")

    # Test case 8: k 很大（大于数组长度）
    nums8 = [1, 2, 3, 1]
    k8 = 10
    result8 = contains_nearby_duplicate(nums8, k8)
    print(f"Test case 8: nums = {nums8}, k = {k8}")
    print(f"Expected: True (索引 0 和 3 的元素相同，距离为 3 <= 10)")
    print(f"Result: {result8}")
    print(f"Pass: {result8 == True}\n")

    # Test case 9: LeetCode 示例
    nums9 = [1, 2, 3, 1, 2, 3]
    k9 = 2
    result9 = contains_nearby_duplicate(nums9, k9)
    print(f"Test case 9: nums = {nums9}, k = {k9}")
    print(f"Expected: False")
    print(f"Result: {result9}")
    print(f"Pass: {result9 == False}\n")

    # Test case 10: 另一个 LeetCode 示例
    nums10 = [99, 99]
    k10 = 2
    result10 = contains_nearby_duplicate(nums10, k10)
    print(f"Test case 10: nums = {nums10}, k = {k10}")
    print(f"Expected: True")
    print(f"Result: {result10}")
    print(f"Pass: {result10 == True}\n")


if __name__ == "__main__":
    main()
