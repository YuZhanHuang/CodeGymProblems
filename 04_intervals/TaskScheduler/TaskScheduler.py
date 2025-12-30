# Task Scheduler

def least_time(tasks, n):
    frq = {}
    for task in tasks:
        frq[task] = 1 + frq.get(task, 0)

    frq = dict(sorted(frq.items(), key=lambda x: x[1]))
    max_frq = frq.popitem()[1]
    idle = (max_frq - 1) * n

    while frq and idle > 0:
        idle -= min(max_frq - 1, frq.popitem()[1])
    
    idle = max(0, idle)

    return len(tasks) + idle


from heapq import *


def least_interval(tasks, n):
    frq = {}
    max_heap = []

    for task in tasks:
        frq[task] = 1 + frq.get(task, 0)

    for key, val in frq.items():
        heappush(max_heap, (-val, key))

    max_frq, _ = heappop(max_heap)
    max_frq = -max_frq

    idle = (max_frq - 1) * n

    while max_heap and idle > 0:
        nxt_max_frq, _ = heappop(max_heap)
        nxt_max_frq = -nxt_max_frq
        idle -= min(max_frq - 1, nxt_max_frq)
    
    idle = max(0, idle)

    return len(tasks) + idle


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
        (["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"], 4, 10),
        (["A", "A", "A"], 2, 7),
        (["A"], 0, 1),
    ]
    
    print("Testing Task Scheduler (least_time):")
    all_passed = True
    for i, (tasks, n, expected) in enumerate(test_cases, 1):
        result = least_time(tasks, n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} least_time({tasks[:10]}{'...' if len(tasks) > 10 else ''}, {n}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}\n")
    
    print("Testing Task Scheduler (least_interval):")
    all_passed = True
    for i, (tasks, n, expected) in enumerate(test_cases, 1):
        result = least_interval(tasks, n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} least_interval({tasks[:10]}{'...' if len(tasks) > 10 else ''}, {n}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

