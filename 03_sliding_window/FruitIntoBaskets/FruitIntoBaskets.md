# Fruit Into Baskets

## Statement

While visiting a farm of fruits, you have been given a row of fruits represented by an integer array, fruits, where fruits[i] is the type of fruit the $i^{th}$ tree produces. You have to collect fruits, but there are some rules that you must follow while collecting fruits:

You are given only two baskets, each capable of holding an unlimited quantity of a single type of fruit.

You can start collecting from any tree but must collect exactly one fruit from each tree (including the starting tree) while moving to the right.

You must stop while encountering a tree with a fruit type that cannot fit into any of your baskets.

Return the maximum number of fruits you can collect following the above rules for the given array of fruits.

## Constraints:

1 ≤ fruits.length ≤ $10^{3}$

0 ≤ fruits[i] < fruits.length

