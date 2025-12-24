# Patterns Index (faceted)

| pattern | paradigm | ds | goal | constraints | risks | complexity |
| --- | --- | --- | --- | --- | --- | --- |
| 03_sliding_window | iteration, two-pointers, sliding-window | array, hash | optimize(min/len), enumerate | window=variable, mutable | 去重、邊界 | O(n), O(k) |
| 06_heaps | heap | heap | top-k, k-th, merge-k | needs comparator | 溢位、比較器 | O(n log k), O(k) |
| 10_subsets | recursion, backtracking | array | enumerate | sorted/unsorted | 去重、分支爆炸 | O(2^n), O(n) |
| 15_topological_sort | DFS, BFS | graph | order, cycle-detect | DAG only | 邊界、入度零 | O(V+E), O(V+E) |
| 25_union_find | union-find | disjoint-set | connectivity | offline/online | 路徑壓縮實作 | α(n), O(n) |

