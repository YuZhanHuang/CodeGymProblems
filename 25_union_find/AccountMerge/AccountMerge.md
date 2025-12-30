# Account Merge

## Statement

You are given a 2D array, accounts, where each row, accounts[i], is an array of strings, such that the first element, accounts[i][0], is a name, while the remaining elements are emails associated with that account. Your task is to determine if two accounts belong to the same person by checking if both accounts have the same name and at least one common email address.

If two accounts have the same name, they might belong to different people since people can have the same name. However, all accounts that belong to one person will have the same name. This implies that a single person can hold multiple accounts.

The output should be a 2D array in which the first element of each row is the name, and the rest of the elements are the merged list of that user's email addresses in sorted order. There should be one row for each distinct user, and for each user, each email address should be listed only once.

**Note**: Please use a sort function that sorts the email addresses based on the ASCII value of each character.

## LeetCode Link

https://leetcode.com/problems/accounts-merge/

## Constraints

- 1 ≤ accounts.length ≤ 100
- 2 ≤ accounts[i].length ≤ 10
- 1 ≤ accounts[i][j].length ≤ 30
- Because accounts[i][0] is the name of any person, it should contain only English letters.
- For j > 0, accounts[i][j] should be a valid email.

