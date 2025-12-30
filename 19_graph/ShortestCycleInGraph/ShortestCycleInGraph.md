# Shortest Cycle in a Graph

## Statement

You are given a bidirectional graph with n vertices, labeled from 0 to n - 1. The graph is represented by a 2D integer array edges, where each element edges[i] = [u_i, v_i] represents an edge connecting vertex u_i and vertex v_i. Each vertex pair has at most one edge between them, and no vertex is connected to itself.

Your task is to find the length of the shortest cycle in the graph. A cycle is defined as a path that starts and ends at the same vertex, with each edge in the path appearing exactly once. If no cycle exists in the graph, return -1.

## Constraints

- 2 ≤ n ≤ 1000
- 1 ≤ edges.length ≤ 1000
- edges.length == 2
- 0 ≤ u_i, v_i < n
- u_i ≠ v_i
- No duplicate edges exist in the graph

