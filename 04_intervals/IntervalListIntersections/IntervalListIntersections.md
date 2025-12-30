# Interval List Intersections

## Statement

For two lists of closed intervals given as input, interval_list_a and interval_list_b, where each interval has its own start and end time, write a function that returns the intersection of the two interval lists.

For example, the intersection of [3, 8] and [5, 10] is [5, 8].

## Constraints

- 0 ≤ interval_list_a.length, interval_list_b.length ≤ 1000
- 0 ≤ start[i] < end[i] ≤ 10^9, where i is used to indicate interval_list_a
- end[i] < start[i + 1]
- 0 ≤ start[j] < end[j] ≤ 10^9, where j is used to indicate interval_list_b
- end[j] < start[j + 1]

