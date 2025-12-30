# Shortest Cycle in a Graph

from collections import defaultdict, deque


# Solution 1: BFS approach
def find_shortest_cycle_bfs(n, edges):
    # initalize variables
    graph = defaultdict(list)
    INF = float('inf')
    answer = INF
    
    # create graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS from each component
    for start in range(n):
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        queue = deque([start])
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    cycle_len = dist[u] + dist[v] + 1
                    answer = min(answer, cycle_len)
            
            if answer == 3:
                return 3
                
    return answer if answer < INF else -1


# Solution 2: DFS approach with backtracking
def shortest_cycle_dfs(n, edges):
    """
    Find the shortest cycle length in an undirected graph using DFS.
    If no cycle exists, return -1.
    
    Parameters:
    - n: Number of nodes (labeled 0..n-1)
    - edges: List of [u, v] undirected edges
    
    Return:
    - Shortest cycle length, or -1 if no cycle exists
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    INF = float('inf')
    ans = INF

    visited = [False] * n

    def dfs(u, parent, start, depth):
        nonlocal ans
        # Prune if depth exceeds current answer
        if depth + 1 >= ans:
            return
        visited[u] = True
        for v in graph[u]:
            if v == parent:
                continue
            if v == start and depth >= 1:
                # Found a cycle: start → ... → u → start
                cycle_len = depth + 1
                ans = min(ans, cycle_len)
            elif not visited[v] and v > start:
                dfs(v, u, start, depth + 1)
        visited[u] = False

    # Only enumerate start as the smallest vertex in the cycle to avoid duplicates
    for start in range(n):
        dfs(start, -1, start, 0)

    return ans if ans < INF else -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 3]], 3),
        (5, [[0, 1], [1, 2], [2, 3]], -1),
        (4, [[0, 1], [1, 2], [2, 3], [3, 0]], 4),
    ]
    
    print("Testing Shortest Cycle in a Graph (BFS):")
    all_passed = True
    for i, (n, edges, expected) in enumerate(test_cases, 1):
        result = find_shortest_cycle_bfs(n, edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_shortest_cycle_bfs(n={n}, ...) = {result}, expected {expected}")
    
    print("\nTesting Shortest Cycle in a Graph (DFS):")
    for i, (n, edges, expected) in enumerate(test_cases, 1):
        result = shortest_cycle_dfs(n, edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} shortest_cycle_dfs(n={n}, ...) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

