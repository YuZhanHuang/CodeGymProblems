# Network Delay Time

from collections import defaultdict
import heapq


def network_delay_time(times, n, k):
    # create graph
    adjancent_dict = defaultdict(list)
    for src, dst, t in times:
        adjancent_dict[src].append((dst, t))

    # greedy view: we need to take the smallest time node
    pq = []
    heapq.heappush(pq, (0, k))
    visited = set()
    delays = 0

    while pq:
        t, node = heapq.heappop(pq)
        if node in visited:
            continue

        visited.add(node)

        # how to track delays is important
        delays = max(delays, t)
        neighbors = adjancent_dict[node]

        for neighbor in neighbors:
            neighbor_node, neighbor_time = neighbor
            if neighbor_node not in visited:
                # how to track delays is important
                new_time = t + neighbor_time
                heapq.heappush(pq, (new_time, neighbor_node))

    return delays if len(visited) == n else -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ]
    
    print("Testing Network Delay Time:")
    all_passed = True
    for i, (times, n, k, expected) in enumerate(test_cases, 1):
        result = network_delay_time(times, n, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} network_delay_time(times, n={n}, k={k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

