# Patterns Overview

## 第一層分類（遞迴導向 vs 非遞迴導向）
- 遞迴導向：10_subsets, 12_backtracking, 13_dynamic_programming, 15_topological_sort(DFS), 19_graph(DFS), 20_tree_depth_first_search, 21_tree_breadth_first_search(DFS 版), 22_trie, 24_knowing_what_to_track, 26_custom_data_structure(遞迴型), 15/19/20/21 亦可用迭代但教學常以遞迴起手。
- 非遞迴導向：01_two_pointers, 02_fast_and_slow_pointers, 03_sliding_window, 04_intervals, 05_in_place_manipulation_of_a_linked_list, 06_heaps, 07_k_way_merge, 08_top_k_element, 09_modified_binary_search, 11_greedy_techniques, 14_cyclic_sort, 16_sort_and_search, 17_matrices, 18_stacks, 23_hash_map, 25_union_find, 27_bitwise_manipulation, 28_math_and_geometry, 21_tree_breadth_first_search(BFS 版), 22_trie(純查找/插入), 26_custom_data_structure(迭代型)。

## 第二層細緻分類建議
- 樹與圖：20_tree_depth_first_search, 21_tree_breadth_first_search, 19_graph, 15_topological_sort, 22_trie, 25_union_find
- 指標與窗口：01_two_pointers, 02_fast_and_slow_pointers, 03_sliding_window, 04_intervals, 11_greedy_techniques, 16_sort_and_search, 17_matrices, 14_cyclic_sort
- 資料結構驅動：06_heaps, 07_k_way_merge, 08_top_k_element, 18_stacks, 23_hash_map, 24_knowing_what_to_track, 26_custom_data_structure
- 搜尋與分治：09_modified_binary_search, 13_dynamic_programming, 10_subsets, 12_backtracking
- 數學與位元：27_bitwise_manipulation, 28_math_and_geometry
- 鏈表操作：05_in_place_manipulation_of_a_linked_list

## 心智圖（簡化 ASCII）
- Patterns
  - 遞迴導向
    - DFS/回溯：10_subsets, 12_backtracking, 15_topological_sort, 19_graph, 20_tree_depth_first_search
    - 記憶化/DP：13_dynamic_programming, 24_knowing_what_to_track
    - 樹/字典樹：22_trie
    - 其他：21_tree_breadth_first_search(DFS 版), 26_custom_data_structure(遞迴型)
  - 非遞迴導向
    - 指標/窗口：01_two_pointers, 02_fast_and_slow_pointers, 03_sliding_window
    - 區間/掃描：04_intervals, 11_greedy_techniques, 16_sort_and_search, 17_matrices, 14_cyclic_sort
    - 堆/優先序：06_heaps, 07_k_way_merge, 08_top_k_element
    - 搜尋/分治：09_modified_binary_search, 13_dynamic_programming(自底向上), 12_backtracking(可迭代 stack)
    - 資料結構：18_stacks, 23_hash_map, 25_union_find, 26_custom_data_structure(迭代型)
    - 數學/位元：27_bitwise_manipulation, 28_math_and_geometry
    - 鏈表：05_in_place_manipulation_of_a_linked_list
    - 樹/圖 BFS：21_tree_breadth_first_search(BFS 版), 19_graph(BFS)

> 提示：可在各 `summary_01.md` 補充「遞迴/非遞迴解法骨架 + 常見陷阱」，並於此檔更新連結以形成目錄。

## 多維標籤導覽
- 範式（paradigm）：DFS / BFS / DP / greedy / divide-and-conquer / two-pointers / sliding-window / heap / union-find
- 資料結構（ds）：array / linked-list / tree / graph / heap / trie / UF / hash / stack-queue / bitset
- 目標（goal）：search / optimize(k-th, top-k, min/max) / order, rank / cover, match / enumerate / connectivity
- 限制（constraints）：sorted/unsorted / static/dynamic / online/offline / mutable/immutable / window-size / DAG/weighted
- 風險（risks）：去重 / 重疊區間 / 溢位 / 深度（遞迴） / 精度（浮點） / 邊界（索引、空集合）

### 分面索引建議
- 依範式反查：列出 DFS/BFS/DP/greedy/two-pointers/sliding-window/heap/union-find 系的題目清單。
- 依資料結構反查：堆系、Trie 系、Union-Find 系、矩陣掃描系、hash + 窗口系。
- 依目標反查：K-th/Top-K、最短/最長、排序/排名、覆蓋/匹配、枚舉生成、連通性。
- 依限制反查：不可修改輸入、需排序預處理、窗口固定/可變、線上/離線、圖是否有向/有權/非負。
- 依風險反查：去重、重疊處理、溢位、遞迴深度、精度、邊界。

## 維護規則
1. 新增題目時，在 `patterns_index.md` / `.json` 標記：paradigm, ds, goal, constraints, risks, complexity。
2. 若同題有多種典型解（如 DFS/BFS），兩個都標並在備註說明取捨。
3. 各 `summary_01.md` 保持三區塊：不變量 / 轉折事件 / 常見陷阱，隨題目練習更新。
4. 每次練習後在對應 dry-run 檔補：spec checkpoints、turning points（事件驅動）、答案更新時機、複雜度來源。
5. 定期整理：把可遷移的觀念寫回該 pattern 的 summary，並在 overview 增加對應分面索引條目。
