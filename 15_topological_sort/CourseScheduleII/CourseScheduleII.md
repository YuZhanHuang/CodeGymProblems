# Course Schedule II

## Statement

Let's assume that there are a total of n courses labeled from 0 to n−1. Some courses may have prerequisites. A list of prerequisites is specified such that if prerequisites[i] = [a[i], b[i]], you must take course b[i] before course a[i].

Given the total number of courses n and a list of the prerequisite pairs, return the course order a student should take to finish all of the courses. If there are multiple valid orderings of courses, then return any one of them.

**Note**: There can be a course in the 0 to n−1 range with no prerequisites.

## LeetCode Link

https://leetcode.com/problems/course-schedule-ii/

## Constraints

- Let n be the number of courses.
- 1 ≤ n ≤ 1500 
- 0 ≤ prerequisites.length ≤ 1000
- prerequisites[i].length == 2
- 0 ≤ a, b < n 
- a ≠ b
- All the pairs [a, b] are distinct.

