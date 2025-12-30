# Clone Graph

## Statement

Given a graph that has nodes with data and a list of neighbors, create a deep copy of the graph. The graph has the following properties:

- Undirected: The edges of the graph are bidirectional.
- Connected: A path will always exist between any two nodes.

In a deep copy, a new instance of every node is created with the same data as in the original graph. Any modifications made to the new graph are not reflected in the original graph.

For simplicity, we are creating a graph using an adjacency list, where the data of each node is represented by its index in the adjacency list. Each list in the adjacency list describes the set of neighbors of a node in the graph. The index in the adjacency list starts from 1. For example, for [[2, 3], [1, 3], [1, 2]], there are three nodes in the graph:

- 1st node (data = 1): Neighbors are 2nd node (data = 2) and 3rd node (data = 3).
- 2nd node (data = 2): Neighbors are 1st node (data = 1) and 3rd node (data = 3).
- 3rd node (data = 3): Neighbors are 1st node (data = 1) and 2nd node (data = 2).

## LeetCode Link

https://leetcode.com/problems/clone-graph/

## Constraints

- 0 ≤ Number of nodes ≤ 100
- 1 ≤ Node.data ≤ 100
- Node.data is unique for each node.
- The graph is undirected, i.e., there are no self-loops or repeated edges.
- The graph is connected, i.e., any node can be visited from a given node.

