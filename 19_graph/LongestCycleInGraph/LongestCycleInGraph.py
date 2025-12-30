# Longest Cycle in a Graph

from collections import deque
from typing import List


# Solution 1: Time-stamp DFS approach
def longest_cycle_dfs(edges):
    n = len(edges)
    visited_time = [-1] * n  
    time = 0
    max_cycle = -1

    for i in range(n):
        if visited_time[i] != -1:
            continue  

        node_to_time = {}
        current = i

        while current != -1 and visited_time[current] == -1:
            node_to_time[current] = time
            visited_time[current] = time
            time += 1
            current = edges[current]

            if current in node_to_time:
                # Found a cycle
                cycle_length = time - node_to_time[current]
                max_cycle = max(max_cycle, cycle_length)
                break

    return max_cycle


# Solution 2: Kahn's algorithm (topological sort) approach
def longest_cycle_kahn(edges: List[int]) -> int:
    n = len(edges)
    indeg = [0]*n
    for u, v in enumerate(edges):
        if v != -1:
            indeg[v] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    removed = [False]*n
    while q:
        u = q.popleft()
        removed[u] = True
        v = edges[u]
        if v != -1:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    ans = -1
    seen = [False]*n  # To avoid counting the same cycle multiple times
    for i in range(n):
        if removed[i] or seen[i]:
            continue
        # Node i must be in a cycle; follow edges to complete the cycle
        cur = i
        length = 0
        while not seen[cur]:
            seen[cur] = True
            length += 1
            cur = edges[cur]
        ans = max(ans, length)

    return ans if ans != 0 else -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 3, 4, 2, 3], 3),
        ([2, -1, 3, 1], -1),
        ([1, 2, 3, 4, 0], 5),
    ]
    
    print("Testing Longest Cycle in a Graph (DFS):")
    all_passed = True
    for i, (edges, expected) in enumerate(test_cases, 1):
        result = longest_cycle_dfs(edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} longest_cycle_dfs({edges}) = {result}, expected {expected}")
    
    print("\nTesting Longest Cycle in a Graph (Kahn's Algorithm):")
    for i, (edges, expected) in enumerate(test_cases, 1):
        result = longest_cycle_kahn(edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} longest_cycle_kahn({edges}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

