# Nested List Weight Sum II

## Statement

Given a nested list of integers, nested_list, where each element can either be an integer or a list, which can contain integers or more lists, return the sum of each integer in nested_list multiplied by its weight.

The weight of an integer is calculated as max_depth minus the depth of the integer plus one.

The depth of an integer is defined as the number of nested lists it is contained within. For instance, the value of each integer in the list [1,[2,2],[[3],2],1] is equal to its depth. Let max_depth represent the maximum depth of any integer in the nested_list.

## Constraints

- 1 ≤ nested_list.length ≤ 50
- The values of the integers in the nested list are in the range [−100,100]
- max_depth ≤ 50

