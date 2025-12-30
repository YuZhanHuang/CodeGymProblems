# Split a Circular Linked List

## Statement

Given a circular linked list, of positive integers, split it into two circular linked lists. The first circular linked list should contain the first half of the nodes (exactly ⌈list.length / 2⌉ nodes) in the same order they appeared in the original list, while the second circular linked list should include the remaining nodes in the same order.

Return an array, answer, of length 2, where:

answer[0] is the head of the circular linked list representing the first half.

answer[1] is the head of the circular linked list representing the second half.

Note: A circular linked list is a standard linked list where the last node points back to the first node.

## Constraints:

Let n be the number of nodes in a linked list.

2 ≤ n ≤ 10^3

0 ≤ Node.value ≤ 10^5

LastNode.next = FirstNode where LastNode is the last node of the list and FirstNode is the first one.

