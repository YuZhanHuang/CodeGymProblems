# Minimum Number of Refueling Stops

import heapq


def min_refuel_stops(target, start_fuel, stations):
    if start_fuel >= target:
        return 0
 
    refuel = []
    count = 0
    i, n = 0, len(stations) - 1
    max_dist = start_fuel

    while max_dist < target:
        if i <= n and max_dist >= stations[i][0]:
            heapq.heappush(refuel, (-stations[i][1], stations[i][0]))
            i += 1
        elif i <= n and max_dist < stations[i][0]:
            if refuel:
                max_dist += -heapq.heappop(refuel)[0]
                count += 1
            else:
                return -1
        else:
            if refuel:
                max_dist += -heapq.heappop(refuel)[0]
                count += 1
            else:
                return -1

    return count


# Test cases
if __name__ == "__main__":
    test_cases = [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
    ]
    
    print("Testing Minimum Number of Refueling Stops:")
    all_passed = True
    for i, (target, start_fuel, stations, expected) in enumerate(test_cases, 1):
        result = min_refuel_stops(target, start_fuel, stations)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} min_refuel_stops(target={target}, start_fuel={start_fuel}, stations={stations}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

