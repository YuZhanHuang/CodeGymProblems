# Minimum Cost to Hire K Workers

import heapq


def min_cost_to_hire_workers(quality, wage, k):
    # 1) Build and sort by each worker's wage/quality ratio
    workers = sorted((w / q, q) for w, q in zip(wage, quality))
    
    max_heap = []    # will store negative qualities
    sum_q = 0        # sum of the k smallest qualities seen so far
    min_cost = float('inf')
    
    # 2) Sweep through workers in increasing ratio order
    for ratio, q in workers:
        # Add this worker's quality to the heap and running sum
        heapq.heappush(max_heap, -q)
        sum_q += q
        
        # If we have more than k workers, eject the one with the highest quality
        if len(max_heap) > k:
            removed_q = -heapq.heappop(max_heap)
            sum_q -= removed_q
        
        # Once we have exactly k workers, compute total cost under this ratio
        if len(max_heap) == k:
            cost = ratio * sum_q
            min_cost = min(min_cost, cost)
    
    return min_cost


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([10, 20, 5], [70, 50, 30], 2, 105.0),
        ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3, 30.666666666666668),
    ]
    
    print("Testing Minimum Cost to Hire K Workers:")
    all_passed = True
    for i, (quality, wage, k, expected) in enumerate(test_cases, 1):
        result = min_cost_to_hire_workers(quality, wage, k)
        status = "✓" if abs(result - expected) < 1e-5 else "✗"
        if abs(result - expected) >= 1e-5:
            all_passed = False
        print(f"Test {i}: {status} min_cost_to_hire_workers(quality={quality}, wage={wage}, k={k}) = {result:.6f}, expected {expected:.6f}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

