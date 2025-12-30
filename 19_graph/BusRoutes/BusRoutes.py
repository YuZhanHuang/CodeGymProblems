# Bus Routes

from collections import deque, defaultdict


def minimum_buses(bus_routes, src, dest):
    # build mapping
    adjacent_list = defaultdict(list)
    for bus, stations in enumerate(bus_routes):
        for station in stations:
            adjacent_list[station].append(bus)

    queue = deque()
    queue.append((src, 0))
    visited_bus = set()

    # use bfs with queue
    while queue:
        station, bus_taken = queue.popleft()
        if station == dest:
            return bus_taken
        buses = adjacent_list.get(station, [])
        for bus in buses:
            if bus not in visited_bus:
                for station in bus_routes[bus]:
                    queue.append((station, bus_taken+1))
                visited_bus.add(bus)

    return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
        ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1),
    ]
    
    print("Testing Bus Routes:")
    all_passed = True
    for i, (routes, src, dest, expected) in enumerate(test_cases, 1):
        result = minimum_buses(routes, src, dest)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} minimum_buses(routes, src={src}, dest={dest}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

