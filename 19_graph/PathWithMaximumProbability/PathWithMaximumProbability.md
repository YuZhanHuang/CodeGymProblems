# Path with Maximum Probability

## Statement

You are given an undirected weighted graph of n nodes, represented by a 0-indexed list, edges, where edges[i] = [a, b] is an undirected edge connecting the nodes a and b. There is another list succProb, where succProb[i] is the probability of success of traversing the edge edges[i].

Additionally, you are given two nodes, start and end. Your task is to find the path with the maximum probability of success to go from start to end and return its success probability. If there is no path from start to end, return 0.

## Constraints

- 2 ≤ n ≤ 10^3
- 0 ≤ start, end < n
- start ≠ end
- 0 ≤ a, b < n
- a ≠ b
- 0 ≤ succProb.length == edges.length ≤ 2×10^3
- 0 ≤ succProb[i] ≤ 1
- There is, at most, one edge between every two nodes.

