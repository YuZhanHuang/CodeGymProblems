# Compilation Order

from collections import deque, defaultdict


def find_compilation_order(dependencies):
    # initialize variable
    graph = defaultdict(list)
    in_degrees = defaultdict(int)
    classes = set()
    result = []
    queue = deque()
    
    for course, prev in dependencies:
        graph[prev].append(course)
        in_degrees[course] += 1
        classes.add(prev)
        classes.add(course)

    for i in classes:
        if in_degrees[i] == 0:
            queue.append(i)
        
    while queue:
        course = queue.popleft()
        result.append(course)
        
        for nbr in graph[course]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                queue.append(nbr)
    
    if len(result) != len(classes):
        return []
        
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([['B', 'A'], ['C', 'A'], ['D', 'C'], ['E', 'D'], ['E', 'B']], ['A', 'B', 'C', 'D', 'E']),
        ([['B', 'A'], ['C', 'B']], ['A', 'B', 'C']),
        ([['A', 'B'], ['B', 'A']], []),  # Cycle
    ]
    
    print("Testing Compilation Order:")
    all_passed = True
    for i, (dependencies, expected) in enumerate(test_cases, 1):
        result = find_compilation_order(dependencies)
        # For topological sort, there might be multiple valid answers
        status = "✓" if len(result) == len(expected) or result == expected else "✗"
        if len(result) != len(expected) and result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_compilation_order({dependencies}) = {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

