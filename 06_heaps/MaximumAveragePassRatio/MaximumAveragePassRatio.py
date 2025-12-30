# Maximum Average Pass Ratio

from heapq import heappush, heappop


def max_average_ratio(classes, extraStudents):
    n = len(classes)
    incr_avg_classes = []
    
    for passi, total in classes:
        delta = (total - passi) / (total * (total + 1))
        heappush(incr_avg_classes, (-delta, passi, total))
    
    while extraStudents > 0:
        best, passi, total = heappop(incr_avg_classes)
        passi += 1
        total += 1
        best = (total - passi) / (total * (total + 1))
        heappush(incr_avg_classes, (-best, passi, total))
        extraStudents -= 1
    
    return sum((passi/total) for _, passi, total in incr_avg_classes) / n


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [3, 5], [2, 2]], 2, 0.78333),
        ([[2, 4], [3, 9], [4, 5], [2, 10]], 4, 0.53485),
    ]
    
    print("Testing Maximum Average Pass Ratio:")
    all_passed = True
    for i, (classes, extraStudents, expected) in enumerate(test_cases, 1):
        result = max_average_ratio(classes, extraStudents)
        # Check if result is within 10^-5 of expected
        status = "✓" if abs(result - expected) < 1e-5 else "✗"
        if abs(result - expected) >= 1e-5:
            all_passed = False
        print(f"Test {i}: {status} max_average_ratio({classes}, {extraStudents}) = {result:.5f}, expected {expected:.5f}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

