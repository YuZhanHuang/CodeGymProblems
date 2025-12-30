# Kth Smallest Prime Fraction

## Statement

You are given a sorted array of unique integers, arr, which includes the number 1 and other prime numbers. You are also given an integer k.

For every index i and j where 0 ≤ i < j < arr.length you can form a fraction by taking the number at index i as the numerator and the number at index j as the denominator, resulting in the fraction arr[i] / arr[j].

Your task is to return the k-th smallest fraction among these fractions. The answer should be returned as an array of two integers, where the first element, answer[0], is the numerator (arr[i]), and the second element, answer[1], is the denominator (arr[j]) corresponding to the k-th smallest fraction.

## LeetCode Link

https://leetcode.com/problems/k-th-smallest-prime-fraction/

## Constraints

- 2 ≤ arr.length ≤ 10^3
- 1 ≤ arr[i] ≤ 3 × 10^4
- arr[0] = 1
- arr[i] is a prime number for i > 0.
- All the numbers of arr are unique and sorted in strictly increasing order.
- 1 ≤ k ≤ arr.length × (arr.length - 1)

