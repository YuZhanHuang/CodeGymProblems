# Height of Binary Tree After Subtree Removal Queries

## Statement

We are given the root of a binary tree with n nodes and an array, queries, of size m. Each query represents the root of a subtree that should be removed from the tree. The task here is to determine the height of the binary tree after each query, i.e., once a subtree is removed. We'll store the updated heights against each query in an array and return it.

**Note**: A tree's height is the number of edges in the longest path from the root to any leaf node in the tree.

A few points to be considered:

- All the values in the tree are unique.
- It is guaranteed that queries[i] will not be equal to the value of the root.
- The queries are independent, so the tree returns to its initial state after each query.

## Constraints

- 2 ≤ n ≤ 500
- 1 ≤ Node.data ≤ n
- m == queries.length
- 1 ≤ m ≤ min(400)
- 1 ≤ queries[i] ≤ n
- queries[i] ≠ root.data

