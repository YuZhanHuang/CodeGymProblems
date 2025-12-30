# Exclusive Time of Functions

## Statement

We are given an integer number, n, representing the number of functions running in a single-threaded CPU, and an execution log, which is essentially a list of strings. Each string has the format `{function id}:{"start" | "end"}:{timestamp}`, indicating that the function with function id either started or stopped execution at the time identified by the timestamp value. Each function has a unique ID between 0 and n−1. Compute the exclusive time of the functions in the program.

**Note**: The exclusive time is the sum of the execution times for all the calls to a specific function.

## LeetCode Link

https://leetcode.com/problems/exclusive-time-of-functions/

## Constraints

- 1 ≤ n ≤ 100
- 1 ≤ logs.length ≤ 500
- 0 ≤ function id < n
- 0 ≤ timestamp ≤ 10^3
- No two start events and two end events will happen at the same timestamp.
- Each function has an end log entry for each start log entry.

