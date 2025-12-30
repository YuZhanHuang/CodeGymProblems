# Build a Matrix with Conditions

## Statement

You are given a positive integer k, and you're also given two conditions:

- A 2D integer array row_conditions of size n, where row_conditions[i] = [above[i], below[i]]. This means that above[i] must appear in a row above below[i] in the final matrix.

- A 2D integer array col_conditions of size m, where col_conditions[i] = [left[i], right[i]]. This means that left[i] must appear in a column to the left of right[i] in the final matrix.

Both arrays contain integers from 1 to k.

Your task is to build a k×k matrix that contains all the integers from 1 to k exactly once, while the remaining cells can be filled with zeros.

The matrix should also satisfy the following conditions:

- For each i from 0 to n−1, the integer above[i] must appear in a row strictly above below[i].
- For each i from 0 to m−1, the integer left[i] must appear in a column strictly to the left of right[i].

Return any matrix that meets these conditions. If no valid matrix exists, return an empty matrix.

## LeetCode Link

https://leetcode.com/problems/build-a-matrix-with-conditions/

## Constraints

- 2 ≤ k ≤ 400
- 1 ≤ row_conditions.length, col_conditions.length ≤ 10^4
- row_conditions[i].length == col_conditions[i].length = 2
- 1 ≤ above[i], below[i], left[i], right[i] ≤ k
- above[i] ≠ below[i]
- left[i] ≠ right[i]

