# Maximize Capital

from heapq import heappop, heappush


def maximum_capital(c, k, capitals, profits):
    capitals_min_heap = []
    profits_max_heap = []
    current_profit = c

    for idx, capital in enumerate(capitals):
        heappush(capitals_min_heap, (capital, idx))
  
    for _ in range(k):
        while capitals_min_heap and capitals_min_heap[0][0] <= current_profit:
            _, idx = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[idx], idx))
    
        if not profits_max_heap:
            break

        profit, _ = heappop(profits_max_heap)
        max_profit = -profit
        current_profit += max_profit
  
    return current_profit


# Test cases
if __name__ == "__main__":
    test_cases = [
        (0, 2, [0, 1, 1], [1, 2, 3], 4),  # Start 0, pick project 0 (profit 1), now 1, pick project 1 or 2 (profit 2 or 3), get 4
        (1, 3, [0, 1, 2], [1, 2, 3], 7),  # Start 1, pick 0(+1)->2, pick 1(+2)->4, pick 2(+3)->7
        (0, 3, [0, 1, 2, 3], [1, 2, 3, 5], 8),  # Start 0, pick 0(+1)->1, pick 1(+2)->3, pick 2(+3)->6 (can't pick 3)
        (2, 1, [1, 1, 2], [1, 2, 3], 5),  # Start 2, can pick projects with capital <=2, pick project 2 (max profit 3), get 2+3=5
    ]
    
    print("Testing Maximize Capital:")
    all_passed = True
    for i, (c, k, capitals, profits, expected) in enumerate(test_cases, 1):
        result = maximum_capital(c, k, capitals, profits)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} maximum_capital(c={c}, k={k}, capitals={capitals}, profits={profits}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

