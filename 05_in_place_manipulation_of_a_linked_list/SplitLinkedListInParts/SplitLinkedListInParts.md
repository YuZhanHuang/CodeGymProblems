# Split Linked List in Parts

## Statement

You are given head of a singly linked list and an integer, k. Your task is to split the linked list into k consecutive parts.

Each part should have a size as equal as possible, with the difference between any two parts being at most 1.

If the list cannot be evenly divided, the earlier parts should have more nodes than the later ones.

Any parts that cannot be filled with nodes should be represented as NULL.

The parts must appear in the same order as in the input-linked list.

Return an array of the k parts, maintaining the specified conditions.

## LeetCode Link

https://leetcode.com/problems/split-linked-list-in-parts/

## Constraints

- The number of nodes in the list is in the range [0, 10^3].
- 0 ≤ Node.value ≤ 10^3
- 1 ≤ k ≤ 50

