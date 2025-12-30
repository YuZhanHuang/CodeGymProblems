# Find the Town Judge


def find_judge(n, trust):
    in_degrees = {i: 0 for i in range(1, n+1)}
    out_degrees = {i: 0 for i in range(1, n+1)}
  
    for a, b in trust:
        in_degrees[b] += 1
        out_degrees[a] += 1
    
    for person in range(1, n+1):
        if in_degrees[person] == (n-1) and out_degrees[person] == 0:
            return person
  
    return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
    ]
    
    print("Testing Find the Town Judge:")
    all_passed = True
    for i, (n, trust, expected) in enumerate(test_cases, 1):
        result = find_judge(n, trust)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_judge(n={n}, trust) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

