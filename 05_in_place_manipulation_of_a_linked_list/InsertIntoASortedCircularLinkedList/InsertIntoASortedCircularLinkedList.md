# Insert into a Sorted Circular Linked List

## Statement

You're given a reference to a node, head, in a circular linked list, where the values are sorted in non-decreasing order. The list is circular, so the last node points to the first node. However, the head can be any node in the list—it is not guaranteed to be the node with the smallest value.

Your task is to insert a new value, insertVal, into the list so that it remains sorted and circular after the insertion.

You can choose any of the multiple valid spots where the value can be inserted while maintaining the sort order.

If the list is empty (i.e., the given node is NULL), create a new circular list with a single node containing insertVal, and return that node.

Otherwise, return the head node after insertion.

## Constraints

- The number of nodes in the list is in the range [0, 10^3].
- −10^3 ≤ Node.val, insertVal ≤ 10^3

