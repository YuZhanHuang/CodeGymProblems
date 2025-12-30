# Find Median from a Data Stream

## Statement

Create a data structure that can store a list of integers that can change in size over time and find the median from this dynamically growing list in constant time, O(1).

Implement a class, MedianOfStream, which should support the following operations:

- **Constructor()**: This initializes the object of this class, which in turn creates the max and the min heap.
- **Insert Num(num)**: This adds an integer, num, to the data structure.
- **Find Median()**: This finds the median of all elements seen so far. If there are an even number of elements, return the average of the two middle values.

## LeetCode Link

https://leetcode.com/problems/find-median-from-data-stream/description/

## Constraints

- -10^5 ≤ num ≤ 10^5, where num is an integer received from the data stream.
- There will be at least one element in the data structure before the median is computed.
- At most, 5 × 10^4 calls will be made to the function that calculates the median.

