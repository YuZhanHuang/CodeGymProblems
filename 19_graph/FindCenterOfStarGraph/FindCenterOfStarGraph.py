# Find Center of Star Graph


# Solution 1: Degree counting approach
def find_center_degree(edges):
    in_degree = {i: 0 for i in range(1, len(edges)+1+1)}
    
    for edge in edges:
        in_degree[edge[1]] += 1
        in_degree[edge[0]] += 1
        
    for node in range(1, len(edges)+1+1):
        if in_degree[node] == len(edges):
            return node
    
    return -1


# Solution 2: Simple comparison approach
# The center node appears in every edge of a star graph
# because it's connected to all other nodes.
# Therefore, the center will be the only node that appears
# more than once in the given edges (specifically in the first two edges).
def find_center(edges):
    first = edges[0]  
    second = edges[1]  

    if first[0] in second:
        return first[0]  
    else:
        return first[1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 3], [4, 2]], 2),
        ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
    ]
    
    print("Testing Find Center of Star Graph (Degree Counting):")
    all_passed = True
    for i, (edges, expected) in enumerate(test_cases, 1):
        result = find_center_degree(edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_center_degree(...) = {result}, expected {expected}")
    
    print("\nTesting Find Center of Star Graph (Simple Comparison):")
    for i, (edges, expected) in enumerate(test_cases, 1):
        result = find_center(edges)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_center(...) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

