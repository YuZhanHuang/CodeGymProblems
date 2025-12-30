# Schedule Tasks on Minimum Machines

import heapq


def minimum_machines(tasks):
    tasks.sort()
    machines = []
    
    for start, end in tasks:
        if machines and start >= machines[0]:
            heapq.heappop(machines)
        
        heapq.heappush(machines, end)
    
    return len(machines)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]], 2),
        ([[1, 3], [3, 5], [5, 7]], 1),
        ([[1, 4], [2, 3], [3, 5]], 2),
        ([[1, 5], [2, 4], [3, 6]], 3),
    ]
    
    print("Testing Schedule Tasks on Minimum Machines:")
    all_passed = True
    for i, (tasks, expected) in enumerate(test_cases, 1):
        result = minimum_machines(tasks)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} minimum_machines({tasks}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

