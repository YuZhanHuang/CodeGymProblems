# Insert Interval

## Statement

Given a sorted list of non overlapping intervals and a new interval, your task is to insert the new interval into the correct position while ensuring that the resulting list of intervals remains sorted and non overlapping. Each interval is a pair of nonnegative numbers, the first being the start time and the second being the end time of the interval.

## LeetCode Link

https://leetcode.com/problems/insert-interval/description/

## Example

**Input:** intervals = [[1,3],[6,9]], newInterval = [2,5]

**Output:** [[1,5],[6,9]]

## Constraints

- 0 ≤ existing_intervals.length ≤ 10^4
- existing_intervals[i].length, new_interval.length == 2
- 0 ≤ start time, end time ≤ 10^4
- The first number should always be less than the second number in each interval.
- The list of intervals is sorted in ascending order based on the first element in every interval.

