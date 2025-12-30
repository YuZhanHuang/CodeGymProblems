# Random Pick with Weight

## Statement

You're given an array of positive integers, weights, where weights[i] is the weight of the ith index.

Write a function, Pick Index(), which performs weighted random selection to return an index from the weights array. The larger the value of weights[i], the heavier the weight is, and the higher the chances of its index being picked.

Suppose that the array consists of the weights [12, 84, 35]. In this case, the probabilities of picking the indexes will be as follows:

- Index 0: 12 / (12 + 84 + 35) = 9.2%
- Index 1: 84 / (12 + 84 + 35) = 64.1%
- Index 2: 35 / (12 + 84 + 35) = 26.7%

## Constraints

- 1 ≤ weights.length ≤ 10^4
- 1 ≤ weights[i] ≤ 10^5
- Pick Index() will be called at most 10^4 times.

