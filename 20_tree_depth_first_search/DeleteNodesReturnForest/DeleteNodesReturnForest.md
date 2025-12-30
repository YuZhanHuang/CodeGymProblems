# Delete Nodes and Return Forest

## Statement

Given the root of a binary tree where each node has a unique value, your task is to delete all nodes with values specified in the delete_nodes list. After performing the deletions, the tree will split into a forest—a collection of disjoint trees. Return the roots of the remaining trees in the forest in any order.

## Constraints

- 0 ≤ nodes ≤ 100
- 1 ≤ nodes.value ≤ 1000
- 0 ≤ delete_nodes.length ≤ 100
- 1 ≤ delete_nodes[i] ≤ 1000
- **Note**: Both nodes and delete_nodes[i] will have distinct values.

