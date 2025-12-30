# The Number of the Smallest Unoccupied Chair

## Statement

At a party, n friends, numbered from 0 to n-1, arrive and leave at different times. There are infinitely many chairs, numbered 0 onwards. Each arriving friend sits on the smallest available chair at that moment.

For example, if chairs 0, 1, and 5 are occupied when a friend arrives, they will sit on chair number 2.

When a friend leaves, their chair becomes immediately available. If another friend arrives simultaneously, they can take that chair.

You are given a 0-indexed 2D list times, where times[i] = [arrival_i, leaving_i] represents the arrival and departure times of the i-th friend. All arrival times are unique.

Given an integer target_friend, return the chair number that target_friend will sit on.

## LeetCode Link

https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

## Constraints

- n == times.length
- times[i].length == 2
- 1 ≤ arrival_i < leaving_i ≤ 10^5
- 0 ≤ target_friend ≤ n-1
- Each arrival_i time is unique.

