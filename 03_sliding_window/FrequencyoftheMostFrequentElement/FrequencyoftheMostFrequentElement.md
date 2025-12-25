# Frequency of the Most Frequent Element

## Statement

You are given an integer array, nums, and an integer k, representing the maximum number of operations you can perform. In each operation, you may select any index in nums and increment its value by 1.

Your task is to determine the maximum possible frequency of a single element in the final array after performing at most k operations. You can choose to increase any elements in a way that results in one particular element appearing as often as possible (within k operations). For example, if nums = [2, 2, 3] and k = 4, you can increment the first and the second element, 2, once to match the third element, 3, achieving a maximum frequency of 3.

Return the highest frequency that can be achieved for any element in nums after at most k operations.

The frequency of an element is the number of times it appears in an array.

## Constraints:

1 ≤ nums.length ≤ $10^{3}$

1 ≤ nums[i] ≤ $10^{3}$

1 ≤ k ≤ $10^{3}$

