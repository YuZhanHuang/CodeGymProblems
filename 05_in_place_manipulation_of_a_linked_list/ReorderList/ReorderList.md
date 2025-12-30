# Reorder List

## Statement

Given the head of a singly linked list, reorder the list as if it were folded on itself. For example, if the list is represented as follows:

L₀ → L₁ → L₂ ... L_{n-2} → L_{n-1} → Lₙ

This is how you'll reorder it:

L₀ → Lₙ → L₁ → L_{n-1} → L₂ → L_{n-2} ...

You don't need to modify the values in the list's nodes; only the links between nodes need to be changed.

## Constraints

- The range of number of nodes in the list is [1, 500].
- −5000 ≤ Node.value ≤ 5000

