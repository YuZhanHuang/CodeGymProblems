# Course Schedule

from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    # Initialize
    graph = defaultdict(list)
    in_degrees = defaultdict(int)
    queue = deque()
    result = []
    
    # create graph and in-degrees
    for course, prev in prerequisites:
        graph[prev].append(course)
        in_degrees[course] += 1
    
    # put no dependency course
    for course in range(num_courses):
        if in_degrees[course] == 0:
            queue.append(course)
    
    # choose course which in-degree == 0 
    while queue:
        course = queue.popleft()
        result.append(course)

        for nbr in graph[course]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                queue.append(nbr)
    
    return len(result) == num_courses


# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (1, [], True),
    ]
    
    print("Testing Course Schedule:")
    all_passed = True
    for i, (num_courses, prerequisites, expected) in enumerate(test_cases, 1):
        result = can_finish(num_courses, prerequisites)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} can_finish({num_courses}, {prerequisites}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

