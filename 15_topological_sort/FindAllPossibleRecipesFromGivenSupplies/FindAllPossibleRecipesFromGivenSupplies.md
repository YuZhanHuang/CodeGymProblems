# Find All Possible Recipes from Given Supplies

## Statement

You are given information about n different recipes. Each recipe is listed in the array recipes, and its corresponding ingredients are provided in the 2D array ingredients. The ith recipe, recipes[i], can be prepared if all the necessary ingredients listed in ingredients[i] are available. Some ingredients might need to be created from other recipes, meaning ingredients[i] may contain strings that are also in recipes.

Additionally, you have a string array supplies that contains all the ingredients you initially have, and you have an infinite supply of each.

Return a list of all the recipes you can create. The answer can be returned in any order.

**Note**: It is possible for two recipes to list each other as ingredients. However, if these are the only two recipes provided, the expected output is an empty list.

## LeetCode Link

https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

## Constraints

- n == recipes.length == ingredients.length
- 1 ≤ n ≤ 100
- 1 ≤ ingredients[i].length, supplies.length ≤ 100
- 1 ≤ recipes[i].length, ingredients[i][j].length, supplies[k].length ≤ 10
- recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
- All the combined values of recipes and supplies are unique.
- Each ingredients[i] doesn't contain any duplicate values.

