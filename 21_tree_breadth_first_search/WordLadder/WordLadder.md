# Word Ladder

## Statement

Given two words, src and dest, and a list, words, return the number of words in the shortest transformation sequence from src to dest. If no such sequence can be formed, return 0.

A transformation sequence is a sequence of words (src → word_1 → word_2 → ... → word_j) that has the following properties:

- word_j = dest
- Every pair of consecutive words differs by a single character.
- All the words in the sequence are present in the words. The src does not need to be present in words.

## LeetCode Link

https://leetcode.com/problems/word-ladder/

## Constraints

- 1 ≤ src.length ≤ 10
- src.length == dest.length == words[i].length
- src ≠ dest
- 1 ≤ words.length ≤ 5000
- No duplicates in the words
- src, dest, and words[i] consist of lowercase English characters.

