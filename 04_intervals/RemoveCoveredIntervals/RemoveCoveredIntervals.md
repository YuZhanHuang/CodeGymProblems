# Remove Covered Intervals

## Statement

Given an array of intervals, where each interval is represented as intervals[i] = [l_i, r_i] (indicating the range from l_i to r_i, inclusive of l_i and exclusive of r_i), remove all intervals that are completely covered by another interval in the list. Return the count of intervals that remain after removing the covered ones.

**Note:** An interval [a, b) is considered covered by another interval [c, d) if and only if c <= a and b <= d.

## LeetCode Link

https://leetcode.com/problems/remove-covered-intervals/

## Constraints

- 1 <= intervals.length <= 1000
- intervals[i].length == 2
- 0 <= l_i < r_i <= 10^5
- All the given intervals are unique.

