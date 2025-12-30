# Employee Free Time

## Statement

You're given a list containing the schedules of multiple employees. Each person's schedule is a list of non-overlapping intervals in sorted order. An interval is specified with the start and end time, both being positive integers. Your task is to find the list of finite intervals representing the free time for all the employees.

**Note:** The common free intervals are calculated between the earliest start time and the latest end time of all meetings across all employees.

## LeetCode Link

https://leetcode.com/problems/employee-free-time/description/

## Constraints

- 1 ≤ schedule.length , schedule[i].length ≤ 50
- 0 ≤ interval.start < interval.end ≤ 10^8, where interval is any interval in the list of schedules.

