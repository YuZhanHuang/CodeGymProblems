# Path with Maximum Probability

from collections import defaultdict
import heapq


def max_probability(n, edges, succProb, start, end):
    # initialize variable
    graph = defaultdict(list)
    distances = [0] * n
    distances[start] = 1
    heap = []  # make it as max heap
    
    # create graph
    for (a, b), p in zip(edges, succProb):
        graph[a].append((b, p))
        graph[b].append((a, p))
    
    # put start into heap
    heapq.heappush(heap, (-1, start))
    
    while heap:
        neg_prob, node = heapq.heappop(heap)
        prob = -neg_prob
        
        if prob < distances[node]:
            continue
        
        # reach the end node
        if node == end:
            return prob
        
        for v, edge_p in graph[node]:
            new_prob = prob * edge_p
            if new_prob > distances[v]:
                distances[v] = new_prob
                heapq.heappush(heap, (-new_prob, v))
                
    return 0


# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2, 0.3),
    ]
    
    print("Testing Path with Maximum Probability:")
    all_passed = True
    for i, (n, edges, succProb, start, end, expected) in enumerate(test_cases, 1):
        result = max_probability(n, edges, succProb, start, end)
        status = "✓" if abs(result - expected) < 0.0001 else "✗"
        if abs(result - expected) >= 0.0001:
            all_passed = False
        print(f"Test {i}: {status} max_probability(...) = {result:.5f}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

