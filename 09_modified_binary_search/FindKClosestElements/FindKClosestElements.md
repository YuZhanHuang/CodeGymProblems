# Find K Closest Elements

## Statement

You are given a sorted array of integers, nums, and two integers, target and k. Your task is to return k number of integers that are close to the target value, target. The integers in the output array should be in a sorted order.

An integer, nums[i], is considered to be closer to target, as compared to nums[j] when |nums[i] - target| < |nums[j] - target|. However, when |nums[i] - target| == |nums[j] - target|, the smaller of the two values is selected.

## LeetCode Link

https://leetcode.com/problems/find-k-closest-elements/

## Constraints

- 1 ≤ k ≤ nums.length
- 1 ≤ nums.length ≤ 10^4
- nums is sorted in ascending order.
- -10^4 ≤ nums[i], target ≤ 10^4

