# Task Scheduler

## Statement

We're given a character array, tasks, where each character represents a unique task. These tasks need to be performed by a single CPU, with each task taking one unit of time. The tasks can be performed in any order. At any given time, a CPU can either perform some task or stay idle.

For the given tasks, we are also provided with a positive integer value, n, which represents the cooling period between any two identical tasks. This means that the CPU must wait for at least n units of time before it performs the same task again. For example, if we have the tasks [A,B,A,C] and n = 2, then after performing the first A task, the CPU will wait for at least 2 units of time to perform the second A task. During these 2 units of time, the CPU can either perform some other task or stay idle.

Given the two input values, tasks and n, find the least number of units of time the CPU will take to perform the given tasks.

## LeetCode Link

https://leetcode.com/problems/task-scheduler/description/

## Example

**Input:** tasks = ["A","A","A","B","B","B"], n = 2

**Output:** 8

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

## Constraints

- 1 <= tasks.length <= 10000
- tasks consists of uppercase English letters.
- 0 <= n

