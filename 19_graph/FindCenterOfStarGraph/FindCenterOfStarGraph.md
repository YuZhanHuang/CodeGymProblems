# Find Center of Star Graph

## Statement

Given an array edges where each element edges[i] = [u_i, v_i] represents an edge between nodes u_i and v_i in an undirected star graph, find the central node of this star graph.

**Note**: A star graph is a graph where one central node is connected to every other node. This implies that a star graph with n nodes has exactly n - 1 edges.

## Constraints

- 3 ≤ n ≤ 10^3
- edges.length == n - 1
- edges[i].length == 2
- 1 ≤ u_i, v_i ≤ n
- u_i ≠ v_i
- The given edges represent a valid star graph.

