# Employee Free Time

from heapq import heappush, heappop


class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"[{self.start}, {self.end}]"
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def employee_free_time(schedule):  
    min_heap = []
    result = []

    for idx, member in enumerate(schedule):
        heappush(min_heap, (member[0].start, idx, 0))
        
    prev = min_heap[0][0]

    while min_heap:
        _, i, j = heappop(min_heap)
        interval = schedule[i][j]
        if interval.start > prev:
            result.append(Interval(prev, interval.start))

        prev = max(prev, interval.end)
        check_idx = len(schedule[i]) - 1  # 最大 index 

        if j+1 <= check_idx:
            interval = schedule[i][j+1]
            heappush(min_heap, (interval.start, i, j+1))

    return result


# Test cases
if __name__ == "__main__":
    # Helper function to create schedules
    def create_schedule(intervals_list):
        return [[Interval(s, e) for s, e in employee] for employee in intervals_list]
    
    # Helper function to create expected result
    def create_intervals(intervals):
        return [Interval(s, e) for s, e in intervals]
    
    test_cases = [
        (
            [[[1, 3], [4, 6]], [[2, 4]], [[3, 4]]],
            []  # No free time: all covered by [1,4] and [4,6] -> [1,6]
        ),
        (
            [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]],
            [[5, 6], [7, 9]]
        ),
        (
            [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]],
            [[3, 4]]
        ),
        (
            [[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]],
            [[4, 6], [8, 9]]
        ),
    ]
    
    print("Testing Employee Free Time:")
    all_passed = True
    for i, (schedule_data, expected_data) in enumerate(test_cases, 1):
        schedule = create_schedule(schedule_data)
        expected = create_intervals(expected_data)
        result = employee_free_time(schedule)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status}")
        if result != expected:
            print(f"  Output:   {result}")
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

