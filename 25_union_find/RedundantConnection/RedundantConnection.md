# Redundant Connection

## Statement

We're given an undirected graph consisting of n nodes. The graph is represented as list called edges, of length n, where edges[i] = [a, b] indicates that there is an edge between nodes a and b in the graph.

Return an edge that can be removed to make the graph a tree of n nodes. If there are multiple candidates for removal, return the edge that occurs last in edges.

## LeetCode Link

https://leetcode.com/problems/redundant-connection/

## Constraints

- 3 ≤ n ≤ 100
- edges.length == n
- edges[i].length == 2
- 1 ≤ a < b ≤ n
- a ≠ b
- There are no repeated edges.
- The given graph is connected.
- The graph contains only one cycle.

