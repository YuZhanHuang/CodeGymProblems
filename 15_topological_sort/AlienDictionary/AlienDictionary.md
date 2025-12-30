# Alien Dictionary

## Statement

In this challenge, you are given a list of words written in an alien language, where the words are sorted lexicographically by the rules of this language. Surprisingly, the aliens also use English lowercase letters, but possibly in a different order.

Given a list of words written in the alien language, you have to return a string of unique letters sorted in the lexicographical order of the alien language as derived from the list of words.

If there's no solution, that is, no valid lexicographical ordering, you can return an empty string.

**Note**: The lexicographic order of a given language is defined by the order in which the letters of its alphabet appear. In English, the letter "n" appears before the letter "r" in the alphabet. As a result, in two words that are the same up to the point where one features "n" and the other features "r," the former is considered the lexicographically smaller word of the two. For this reason, "ban" is considered lexicographically smaller than "bar."

Similarly, if an input contains words followed by their prefix, such as "educated" and then "educate," these cases will never result in a valid alphabet because in a valid alphabet, prefixes are always first.

## LeetCode Link

https://leetcode.com/problems/alien-dictionary/

## Constraints

- 1 ≤ words.length ≤ 10^3
- 1 ≤ words[i].length ≤ 20
- All characters in words[i] are English lowercase letters.

