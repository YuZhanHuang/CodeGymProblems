# Maximum Twin Sum of a Linked List

## Statement

In a linked list with an even number of nodes (n), each node at position i (using 0−based indexing) is paired with the node at position (n−1−i). These pairs are called twins for all 0 ≤ i < n/2.

For example, if n=4, the twin pairs are:

The node at index 0 pairs with the node at index 3.

The node at index 1 pairs with the node at index 2.

The twin sum is the sum of a node's value and its twin's value. Given the head of a linked list with an even number of nodes, return the maximum twin sum among all pairs.

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

## Constraints:

The list contains an even number of nodes in the range [2, 10^3].

1 ≤ Node.value ≤ 10^3

