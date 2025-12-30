# Paths in Maze That Lead to Same Room

from collections import defaultdict


# Solution 1: DFS backtracking approach
def find_cycles_of_length_three_dfs(corridors):
    # 1. Build undirected graph
    graph = defaultdict(list)
    for u, v in corridors:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(start, current, depth, visited):
        """
        Return number of ways to walk exactly `3` edges starting
        at `start` and ending back at `start`, without repeating
        any intermediate node.
        - depth: how many edges we've taken so far.
        - visited: set of nodes already on the current path.
        """
        # If we've taken 3 edges, check if we're back at start
        if depth == 3:
            return 1 if current == start else 0

        count = 0
        # If we're at depth 2, the only valid next move to form a 3‐cycle
        # is directly back to start.
        if depth == 2:
            for nbr in graph[current]:
                if nbr == start:
                    count += 1
            return count

        # Otherwise (depth 0 or 1), we can go to any unvisited neighbor
        for nbr in graph[current]:
            if nbr not in visited:
                visited.add(nbr)
                count += dfs(start, nbr, depth + 1, visited)
                visited.remove(nbr)
        return count

    total = 0
    # Launch from each node as "start"
    for node in graph:
        total += dfs(node, node, 0, {node})

    # Each triangle is counted 3 (start choices) × 2 (CW vs CCW) = 6 times
    return total // 6


# Solution 2: Intersection-based approach (more efficient)
def number_of_paths(n, corridors):
    room_graph = defaultdict(set)
    confusion = 0
    for room1, room2 in corridors:
        room_graph[room1].add(room2)
        room_graph[room2].add(room1)
        confusion += len(room_graph[room1].intersection(room_graph[room2]))

    return confusion


# Test cases
if __name__ == "__main__":
    test_cases = [
        (5, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 3]], 2),
        (4, [[1, 2], [2, 3], [3, 4], [4, 1]], 0),
    ]
    
    print("Testing Paths in Maze That Lead to Same Room (DFS):")
    all_passed = True
    for i, (n, corridors, expected) in enumerate(test_cases, 1):
        result = find_cycles_of_length_three_dfs(corridors)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_cycles_of_length_three_dfs(...) = {result}, expected {expected}")
    
    print("\nTesting Paths in Maze That Lead to Same Room (Intersection):")
    for i, (n, corridors, expected) in enumerate(test_cases, 1):
        result = number_of_paths(n, corridors)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} number_of_paths(n={n}, ...) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

