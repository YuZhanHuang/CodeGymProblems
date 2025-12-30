# Build a Matrix with Conditions

from collections import defaultdict


def build_matrix(k, row_conditions, col_conditions):
    # using topological sort (ts)
    # two kind of topological sort
    # row ts
    row_ts = ts(row_conditions, k)
    
    # col ts
    col_ts = ts(col_conditions, k)
    
    # declare matrix
    matrix = [[0] * k for _ in range(k)]
    
    # one of ts order fail -> []
    if not row_ts or not col_ts:
        return []
    
    # due to post order traversal -> create mapping value to index
    pos_row = {num: i for i, num in enumerate(row_ts)}
    pos_col = {num: i for i, num in enumerate(col_ts)}
    
    # replace value
    for num in range(1, k+1):
        if num in pos_row and num in pos_col:
            matrix[pos_row[num]][pos_col[num]] = num            

    return matrix


def ts(edges, n):
    # create graph
    graph = defaultdict(list)
    
    for x, y in edges:
        graph[x].append(y)
    
    # mark visited
    # unvisited = 0, visiting = 1, done = 2
    visited = [0] * (n + 1)
    
    order = []

    for i in range(1, n+1):
        if visited[i] == 0:
            if dfs(i, visited, order, graph):
                return []
            
    order.reverse()
    
    return order
    
    
def dfs(node, visited, order, graph):
    # detect cycle
    if visited[node] == 1:
        return True
    # passover visited node
    if visited[node] == 2:
        return False
    
    visited[node] = 1
    for nbr in graph[node]:
        if dfs(nbr, visited, order, graph):
            return True
    visited[node] = 2
    order.append(node)
    
    return False


# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], True),  # Valid matrix exists
        (3, [[1, 2], [2, 3], [3, 1]], [[2, 1]], False),  # Cycle in row conditions
    ]
    
    print("Testing Build a Matrix with Conditions:")
    all_passed = True
    for i, (k, row_cond, col_cond, should_exist) in enumerate(test_cases, 1):
        result = build_matrix(k, row_cond, col_cond)
        has_result = len(result) > 0
        status = "✓" if has_result == should_exist else "✗"
        if has_result != should_exist:
            all_passed = False
        print(f"Test {i}: {status} build_matrix(k={k}, ...) returned {'valid matrix' if has_result else 'empty matrix'}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

