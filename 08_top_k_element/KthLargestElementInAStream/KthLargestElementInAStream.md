# Kth Largest Element in a Stream

## Statement

Given an infinite stream of integers (sorted or unsorted), nums, design a class to find the kth largest element in a stream.

The class should have the following functions, inputs, and return values:

**Init()**: It takes an array of integers and an integer k and initializes the class object.

**Add(value)**: It takes one integer value, appends it to the stream, and returns the element representing the kth largest element in the stream.

## Constraints

- 1 ≤ k ≤ 10^3
- 0 ≤ nums.length ≤ 10^3
- -10^3 ≤ nums[i] ≤ 10^3
- -10^3 ≤ value ≤ 10^3
- At most 10^3 calls will be made to add.
- It is guaranteed that there will be at least k elements in the array when you search for the kth element.

