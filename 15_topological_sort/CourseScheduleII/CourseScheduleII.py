# Course Schedule II

from collections import defaultdict, deque


def find_order(n, prerequisites):
    # prerequisites[i] = [a, b] -> take course b before course a
    # Initialize Variable
    # create graph and in-degrees counter
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    queue = deque()
    result = []
    
    for course, prev in prerequisites:
        graph[prev].append(course)
        in_degree[course] += 1
        
    # pick in_degree == 0
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # choose no dependency 
    while queue:
        course = queue.popleft()
        result.append(course)
        # minus 1 for all related course
        for nbr in graph[course]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    
    if len(result) != n:
        return []
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),
        (1, [], [0]),
    ]
    
    print("Testing Course Schedule II:")
    all_passed = True
    for i, (n, prerequisites, expected) in enumerate(test_cases, 1):
        result = find_order(n, prerequisites)
        # Check if result is valid (has correct length)
        status = "✓" if len(result) == len(expected) else "✗"
        if len(result) != len(expected):
            all_passed = False
        print(f"Test {i}: {status} find_order({n}, {prerequisites}) = {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

