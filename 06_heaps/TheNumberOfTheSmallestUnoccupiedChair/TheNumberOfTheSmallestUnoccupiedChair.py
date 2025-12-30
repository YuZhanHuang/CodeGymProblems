# The Number of the Smallest Unoccupied Chair

import heapq


def smallest_chair(times, target_friend):
    sorted_friends = sorted(enumerate(times), key=lambda x: x[1][0])

    available_chairs = []
    occupied_chairs = []

    chair_index = 0

    for friend_id, (arrival, leaving) in sorted_friends:
        while occupied_chairs and occupied_chairs[0][0] <= arrival:
            _, freed_chair = heapq.heappop(occupied_chairs)
            heapq.heappush(available_chairs, freed_chair)

        if available_chairs:
            assigned_chair = heapq.heappop(available_chairs)
        else:
            assigned_chair = chair_index
            chair_index += 1

        heapq.heappush(occupied_chairs, (leaving, assigned_chair))

        if friend_id == target_friend:
            return assigned_chair


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 4], [2, 3], [4, 6]], 1, 1),
        ([[3, 10], [1, 5], [2, 6]], 0, 2),
    ]
    
    print("Testing The Number of the Smallest Unoccupied Chair:")
    all_passed = True
    for i, (times, target_friend, expected) in enumerate(test_cases, 1):
        result = smallest_chair(times, target_friend)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} smallest_chair({times}, {target_friend}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

