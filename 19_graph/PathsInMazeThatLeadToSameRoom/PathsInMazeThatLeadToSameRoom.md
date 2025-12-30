# Paths in Maze That Lead to Same Room

## Statement

A maze consists of n rooms numbered from 1−n, and some rooms are connected by corridors. You are given a 2D integer array, corridors, where corridors[i]=[room1, room2] indicates that there is a corridor connecting room1 and room2, allowing a person in the maze to go from room1 to room2 and vice versa.

The designer of the maze wants to know how confusing the maze is. The confusion score of the maze is the number of different cycles of length 3.

For example, 1→2→3→1 is a cycle of length 3, but 1→2→3→4 and 1→2→3→2→1 are not.

Two cycles are considered to be different if one or more of the rooms visited in the first cycle is not in the second cycle.

Return the confusion score of the maze.

## Related LeetCode Problems

While LeetCode doesn't have a direct "count all length-3 cycles" problem, here are two closely related cycle problems:

- 2360. Longest Cycle in a Graph (find the maximum-length cycle in a directed graph) (LeetCode, Medium)
- 2509. Cycle Length Queries in a Tree (support edge additions and report cycle lengths, including triangles) (LeetCode)

## Constraints

- 2 ≤ n ≤ 1000
- 1 ≤ corridors.length ≤ 5 * 10^4
- corridors[i].length = 2
- 1 ≤ room1_i, room2_i ≤ n
- room1_i ≠ room2_i
- There are no duplicate corridors.

