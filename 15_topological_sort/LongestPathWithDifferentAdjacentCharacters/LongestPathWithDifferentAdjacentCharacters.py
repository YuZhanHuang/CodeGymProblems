# Longest Path with Different Adjacent Characters

from collections import deque


def longest_path(parent, s):
    # using in-degree == 0 which node is leaf
    # we start from leaf
    n = len(s)
    in_degrees = [0] * n
    queue = deque()
    longest_chains = [[0, 0] for _ in range(n)]
    longest_path_len = 1
    
    for idx in range(1, n):
        in_degrees[parent[idx]] += 1
        
    # put all leaf into queue
    for node in range(n):
        if in_degrees[node] == 0:
            longest_chains[node][0] = 1
            queue.append(node)
    
    # topological sort
    while queue:
        curr = queue.popleft()
        par = parent[curr]
        if par != -1:
            longest_from_curr = longest_chains[curr][0]
            
            if s[curr] != s[par]:
                if longest_from_curr > longest_chains[par][0]:
                    longest_chains[par][1] = longest_chains[par][0]
                    longest_chains[par][0] = longest_from_curr
                elif longest_from_curr > longest_chains[par][1]:
                    longest_chains[par][1] = longest_from_curr
            
            longest_path_len = max(longest_path_len, longest_chains[par][0] + longest_chains[par][1] + 1)
            
            in_degrees[par] -= 1
            if in_degrees[par] == 0:
                longest_chains[par][0] += 1
                queue.append(par)
    
    return longest_path_len


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 0, 1, 1, 2], "abacbe", 3),
        ([-1, 0, 0, 0], "aabc", 3),
        ([-1, 0, 1], "aab", 2),
    ]
    
    print("Testing Longest Path with Different Adjacent Characters:")
    all_passed = True
    for i, (parent, s, expected) in enumerate(test_cases, 1):
        result = longest_path(parent, s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} longest_path(parent, s='{s}') = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

