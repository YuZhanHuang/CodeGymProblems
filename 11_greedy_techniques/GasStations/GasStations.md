# Gas Stations

## Statement

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. We have a car with an unlimited gas tank, and it costs cost[i] of gas to travel from the ith station to the next (i+1)th station. We begin the journey with an empty tank at one of the gas stations.

Find the index of the gas station in the integer array gas such that if we start from that index we may return to the same index by traversing through all the elements, collecting gas[i] and consuming cost[i].

If it is not possible, return -1.

If there exists such index, it is guaranteed to be unique.

## LeetCode Link

https://leetcode.com/problems/gas-station/

## Constraints

- gas.length == cost.length
- 1 ≤ gas.length, cost.length ≤ 10^3
- 0 ≤ gas[i], cost[i] ≤ 10^3

