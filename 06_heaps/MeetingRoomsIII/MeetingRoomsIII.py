# Meeting Rooms III

import heapq


def most_booked(meetings, rooms):
    count = [0] * rooms
    available = list(range(rooms))
    used_rooms = []

    meetings.sort()
    for start_time, end_time in meetings:
        while used_rooms and used_rooms[0][0] <= start_time:
            ending, room = heapq.heappop(used_rooms)
            heapq.heappush(available, room)

        if not available:
            end, room = heapq.heappop(used_rooms)
            end_time = end + (end_time - start_time)
            heapq.heappush(available, room)

        room = heapq.heappop(available)
        heapq.heappush(used_rooms, (end_time, room))
        count[room] += 1

    return count.index(max(count))


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[0, 10], [1, 5], [2, 7], [3, 4]], 2, 0),
        ([[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 3, 1),
    ]
    
    print("Testing Meeting Rooms III:")
    all_passed = True
    for i, (meetings, rooms, expected) in enumerate(test_cases, 1):
        result = most_booked(meetings, rooms)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} most_booked({meetings}, {rooms}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

