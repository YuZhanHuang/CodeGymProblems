# Graph Valid Tree

from collections import defaultdict
from typing import List


# Solution 1: Cycle detection with DFS
def has_cycle_undirected(n: int, edges: List[List[int]]) -> bool:
    """
    n: Number of nodes (0..n-1)
    edges: Edge list, each edge [u, v] represents u <-> v
    Return: True if the graph contains a cycle
    """
    # 1. Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    # 2. Recursive DFS, parent is used to avoid treating the just-visited edge as a cycle
    def dfs(u: int, parent: int) -> bool:
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                # Already visited and not from parent, means there's a cycle
                return True
        return False

    # 3. The graph may be disconnected, need to launch DFS from each unvisited node
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False


# Solution 2: Simple connectivity check (more efficient for tree validation)
def valid_tree(n, edges):
    # A tree with n nodes must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    adjacency = [[] for _ in range(n)]
    for x, y in edges:
        adjacency[x].append(y)
        adjacency[y].append(x)

    visited = {0}
    stack = [0]

    while stack:
        node = stack.pop()
        for neighbour in adjacency[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return len(visited) == n


# Test cases
if __name__ == "__main__":
    test_cases = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ]
    
    print("Testing Graph Valid Tree (Cycle Detection):")
    all_passed = True
    for i, (n, edges, expected) in enumerate(test_cases, 1):
        has_cycle = has_cycle_undirected(n, edges)
        result = not has_cycle and len(edges) == n - 1
        # Also check connectivity
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        def dfs_count(u):
            visited[u] = True
            count = 1
            for v in adj[u]:
                if not visited[v]:
                    count += dfs_count(v)
            return count
        if n > 0 and not has_cycle:
            connected = dfs_count(0) == n
            result = result and connected
        
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} has_cycle_undirected(n={n}, ...) = {result}, expected {expected}")
    
    print("\nTesting Graph Valid Tree (Simple Check):")
    for i, (n, edges, expected) in enumerate(test_cases, 1):
        result = valid_tree(n, edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} valid_tree(n={n}, ...) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

