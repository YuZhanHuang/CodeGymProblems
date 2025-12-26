from collections import deque
from typing import List


def find_max_sliding_window(nums: List[int], w: int) -> List[int]:
    n = len(nums)
    if w > n:
        return [max(nums)]

    result = []
    dq = deque()

    for i in range(n):
        # 移除已超出窗口範圍的元素
        if dq and dq[0] < i - w + 1:
            dq.popleft()

        # 移除佇列中小於當前元素的索引，以保持佇列的遞減性
        # nums[dq[0]] ≥ nums[dq[1]] ≥ … ≥ nums[dq[-1]]
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 將當前元素的索引加入佇列
        dq.append(i)

        # 當窗口滿足條件後，將最大值加入結果
        if i >= w - 1:
            result.append(nums[dq[0]])

    return result


# Driver code
def main():
    # Test case 1: Increasing sequence
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    w1 = 3
    result1 = find_max_sliding_window(nums1, w1)
    expected1 = [3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: Decreasing sequence
    nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    w2 = 3
    result2 = find_max_sliding_window(nums2, w2)
    expected2 = [10, 9, 8, 7, 6, 5, 4, 3]
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: Array with negative numbers
    nums3 = [-1, -3, -5, -7, -9]
    w3 = 2
    result3 = find_max_sliding_window(nums3, w3)
    expected3 = [-1, -3, -5, -7]
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Window size greater than array length
    nums4 = [1, 2, 3, 4]
    w4 = 10
    result4 = find_max_sliding_window(nums4, w4)
    expected4 = [4]
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Window size of 1 (each element is its own max)
    nums5 = [3, 1, 4, 1, 5, 9, 2, 6]
    w5 = 1
    result5 = find_max_sliding_window(nums5, w5)
    expected5 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
