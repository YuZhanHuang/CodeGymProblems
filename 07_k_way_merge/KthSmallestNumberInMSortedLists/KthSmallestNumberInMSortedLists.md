# Kth Smallest Number in M Sorted Lists

## Statement

Given an m number of sorted lists in ascending order and an integer, k, find the k-th smallest number among all the given lists.

Although there can be repeating values in the lists, each element is considered unique and, therefore, contributes to calculating the k-th smallest element.

If k is greater than the total number of elements in the input lists, return the greatest element from all the lists, and if there are no elements in the input lists, return 0.

## Constraints

- 1 ≤ m ≤ 300
- 0 ≤ list[i].length ≤ 300
- -10^9 ≤ list[i][j] ≤ 10^9
- 1 ≤ k ≤ 10^9

