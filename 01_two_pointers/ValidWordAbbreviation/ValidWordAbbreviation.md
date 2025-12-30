# Valid Word Abbreviation

## Statement

Given a string word and an abbreviation abbr, return TRUE if the abbreviation matches the given string. Otherwise, return FALSE.

A certain word "calendar" can be abbreviated as follows:

- "cal3ar" ("cal end ar" skipping three characters "end" from the word "calendar" still matches the provided abbreviation)
- "c6r" ("c alenda r" skipping six characters "alenda" from the word "calendar" still matches the provided abbreviation)

The following are not valid abbreviations:

- "c06r" (has leading zeroes)
- "cale0ndar" (replaces an empty string)
- "c24r" ("c al enda r" the replaced substrings are adjacent)

## LeetCode Link

https://leetcode.com/problems/valid-word-abbreviation/

## Constraints

- 1 ≤ word.length ≤ 20
- word consists of only lowercase English letters.
- 1 ≤ abbr.length ≤ 10
- abbr consists of lowercase English letters and digits.
- All the integers in abbr will fit in a 32–bit integer.

