# Diet Plan Performance

## Statement

A dieter consumes calories[i] calories on the i-th day.

Given an integer k, the dieter reviews their calorie intake over every sequence of k consecutive days (from calories[i] to calories[i+k-1] for all 0 <= i <= n-k). For each sequence, they calculate T, the total calories consumed over those k days:

If T is less than lower, the dieter performs poorly and loses 1 point.

If T is greater than upper, the dieter performs better and gains 1 point.

If T is between lower and upper (inclusive), the dieter's performance is normal, and their points remain the same.

The dieter starts with zero points. Return the total points after the dieter follows this routine for all calories.length days. The total points can be negative.

## Constraints

1 ≤ k ≤ calories.length ≤ $10^{5}$

0 ≤ calories[i] ≤ 20000

0 ≤ lower ≤ upper

