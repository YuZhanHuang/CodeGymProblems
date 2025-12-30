# Find if Path Exists in Graph

## Statement

Given a 2D list, edges, which represents a bidirectional graph. Each vertex is labeled from 0 to n−1, and each edge in the graph is represented as a pair, [x[i], y[i]], showing a bidirectional edge between x[i] and y[i]. Each pair of vertices is connected by at most one edge, and no vertex is connected to itself.

Determine whether a valid path exists from the source vertex to the destination vertex. If it exists, return TRUE; otherwise, return FALSE.

## LeetCode Link

https://leetcode.com/problems/find-if-path-exists-in-graph/

## Constraints

- 1 ≤ n ≤ 10^2
- 0 ≤ edges.length ≤ n(n−1)/2
- edges[i].length = 2
- 0 ≤ x[i], y[i] ≤ n−1
- x[i] ≠ y[i]
- 0 ≤ source, destination ≤ n−1
- There are no duplicate edges.
- There are no self-edges.

