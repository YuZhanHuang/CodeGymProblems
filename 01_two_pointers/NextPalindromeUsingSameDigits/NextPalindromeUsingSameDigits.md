# Next Palindrome Using Same Digits

## Statement

Given a string num_str representing a palindrome, the string only contains digits. Your task is to return the next possible palindrome using the same digits. The returned palindrome would be the next largest palindrome, meaning there can be more than one way to rearrange the digits to make a larger palindrome. Return an empty string if no greater palindrome can be made.

Consider the following example to understand the expected output for a given numeric string:

- input string = "123321"
- possible palindromes = "213312", "231132", "312213", "132231", "321123"
- We should return the palindrome "132231" as it is greater than "123321" yet the smallest palindrome excluding the original palindrome.

## LeetCode Link

https://leetcode.com/problems/next-palindrome-using-same-digits/

## Constraints

- 1 ≤ num.length ≤ 10^5
- num_str is a palindrome.

