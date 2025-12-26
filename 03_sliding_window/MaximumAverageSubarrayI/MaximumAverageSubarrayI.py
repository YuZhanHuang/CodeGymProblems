def find_max_average(nums, k):
    current_sum = sum(nums[0:k])
    max_sum = sum(nums[0:k])

    for i in range(k, len(nums)):
        new_sum = current_sum + nums[i] - nums[i - k]
        if new_sum > max_sum:
            max_sum = new_sum
        current_sum = new_sum

    return max_sum / k


# Driver code
def main():
    # Test case 1: Positive numbers
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    result1 = find_max_average(nums1, k1)
    expected1 = 12.75  # [12,-5,-6,50] = 51/4
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: All same numbers
    nums2 = [5, 5, 5, 5, 5]
    k2 = 3
    result2 = find_max_average(nums2, k2)
    expected2 = 5.0  # Any window gives 5.0
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: Negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    result3 = find_max_average(nums3, k3)
    expected3 = -1.5  # [-1,-2] = -3/2
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: k equals array length
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    result4 = find_max_average(nums4, k4)
    expected4 = 3.0  # [1,2,3,4,5] = 15/5
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Large numbers
    nums5 = [0, 1, 1, 3, 3]
    k5 = 4
    result5 = find_max_average(nums5, k5)
    expected5 = 2.0  # [1,1,3,3] = 8/4
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
