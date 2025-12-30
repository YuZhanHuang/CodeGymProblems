# Network Delay Time

## Statement

A network of n nodes labeled 1 to n is provided along with a list of travel times for directed edges represented as times[i] = (x_i, y_i, t_i), where x_i is the source node, y_i is the target node, and t_i is the delay time from the source node to the target node.

Considering we have a starting node, k, we have to determine the minimum time required for all the remaining n − 1 nodes to receive the signal.

Return −1 if it's not possible for all n−1 nodes to receive the signal.

## LeetCode Link

https://leetcode.com/problems/network-delay-time/

## Constraints

- 1 ≤ k ≤ n ≤ 100
- 1 ≤ times.length ≤ 6000
- times[i].length == 3
- 1 ≤ x, y ≤ n
- x != y
- 0 ≤ t ≤ 100
- Unique pairs of (x, y), which means that there should be no multiple edges

