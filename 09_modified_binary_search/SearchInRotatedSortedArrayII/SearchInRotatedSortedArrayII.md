# Search in Rotated Sorted Array II

## Statement

You are required to find an integer value target in an array arr of non-distinct integers. Before being passed as input to your search function, arr has been processed as follows:

1. It has been sorted in non-descending order.
2. It has been rotated around some pivot k, such that, after rotation, it looks like this: [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. For example, [10, 30, 40, 42, 42, 47, 78, 90, 901], rotated around pivot k=5 becomes [47, 78, 90, 901, 10, 30, 40, 42, 42].

Return TRUE if target exists in the rotated, sorted array arr, and FALSE otherwise, while minimizing the number of operations in the search.

**Note**: In this problem, the value of k is not passed to your search function.

## Constraints

- 1 ≤ arr.length ≤ 1000
- -10^4 ≤ arr[i] ≤ 10^4
- arr is guaranteed to be rotated at some pivot index.
- -10^4 ≤ target ≤ 10^4

