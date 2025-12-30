# Flood Fill

## Statement

We are given the following values as input to begin with:

- The coordinates of a source cell, i.e., sr and sc.
- A target value, target.
- An (m×n) grid.

Our task is to perform flood fill by updating the values of the four directionally connected cells, which have the same value as the source cell with the target value.

**How to perform flood fill:**

Suppose that a (4×4) grid has a source value of 1 at coordinates [1,1]. We perform flood fill on its neighboring cells only if they have the same source value as this cell. Once all adjacent cells are updated, return the new grid after performing flood fill.

If no neighboring cell has a value equal to the source cell, only update the source cell with the target value and return the updated grid.

## LeetCode Link

https://leetcode.com/problems/flood-fill/

## Constraints

- 1 ≤ grid.length, grid[i].length ≤ 50
- 0 ≤ grid[i][j], target ≤ 2^16
- 0 ≤ sr < grid.length
- 0 ≤ sc < grid[i].length

