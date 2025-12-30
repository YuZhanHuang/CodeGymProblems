# Longest Happy String

## Statement

A string is considered happy if it meets the following conditions:

- It comprises only the characters 'a', 'b', and 'c'.
- It does not contain the substrings "aaa", "bbb", or "ccc".
- The total occurrences of:
  - The character 'a' does not exceed a.
  - The character 'b' does not exceed b.
  - The character 'c' does not exceed c.

You are given three integers, a, b, and c, representing the maximum allowable occurrences of 'a', 'b', and 'c', respectively. Your task is to return the longest possible happy string. If there are multiple valid longest happy strings, return any one of them. If no such string can be formed, return an empty string "".

**Note:** A substring is a contiguous sequence of characters within a string.

## LeetCode Link

https://leetcode.com/problems/longest-happy-string/

## Constraints

- 0 ≤ a, b, c ≤ 100
- a + b + c > 0

