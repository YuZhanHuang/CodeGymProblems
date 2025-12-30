# Reconstruct Itinerary

from collections import defaultdict


def find_itinerary(tickets):
    # initialize variable
    graph = defaultdict(list)
    result = []
    
    # create graph
    for src, dst in tickets:
        graph[src].append(dst)
        
    # make dst lexical order (reverse for pop())
    for src in graph:
        graph[src].sort(reverse=True)
    
    dfs("JFK", graph, result)
    
    return result[::-1]


def dfs(curr, graph, result):
    dests = graph[curr]
    
    while dests:
        nxt_dest = dests.pop()
        dfs(nxt_dest, graph, result)
    
    result.append(curr)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
         ["JFK", "MUC", "LHR", "SFO", "SJC"]),
        ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
         ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    ]
    
    print("Testing Reconstruct Itinerary:")
    all_passed = True
    for i, (tickets, expected) in enumerate(test_cases, 1):
        result = find_itinerary(tickets)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_itinerary(...) = {result}")
        print(f"        expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

