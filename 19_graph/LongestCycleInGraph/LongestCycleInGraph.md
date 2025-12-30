# Longest Cycle in a Graph

## Statement

You are given a directed graph with n nodes, labeled from 0 to n - 1. Each node in the graph has at most one outgoing edge.

The graph is described using a 0-indexed integer array edges of length n, where:

- edges[i] represents a directed edge from node i to node edges[i].
- If node i has no outgoing edge, then edges[i] == -1.

Your task is to find the longest cycle length in the graph. If no cycle exists, return -1.

**Note**: A cycle is defined as a path that starts and ends at the same node, following the direction of the edges.

## LeetCode Link

https://leetcode.com/problems/longest-cycle-in-a-graph/

## Constraints

- n == edges.length
- 2 ≤ n ≤ 10^5
- −1 ≤ edges[i] ≤ n
- edges[i] ≠ i

