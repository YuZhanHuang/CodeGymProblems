# Reorganize String

import heapq


def reorganize_string(str):
    counter = {}
    result = ''
    for s in str:
        counter[s] = 1 + counter.get(s, 0)
        
    max_heap = [(-val, key) for key, val in counter.items()]  
    heapq.heapify(max_heap)

    # Very Important Boundary Condition
    if -max_heap[0][0] > (len(str) + 1) // 2:
        return ''
    
    prev_freq, prev_char = 0, None
    
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result += char
        if prev_freq:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        
        prev_freq, prev_char = freq + 1, char

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("aab", "aba"),
        ("aaab", ""),
        ("programming", None),  # Any valid reorganization
    ]
    
    print("Testing Reorganize String:")
    all_passed = True
    for i, test_case in enumerate(test_cases, 1):
        if len(test_case) == 2:
            s, expected = test_case
            result = reorganize_string(s)
            if expected is None:
                # Check if result is valid (no adjacent same chars)
                is_valid = all(result[j] != result[j+1] for j in range(len(result)-1)) if result else False
                status = "✓" if is_valid else "✗"
                if not is_valid:
                    all_passed = False
                print(f"Test {i}: {status} reorganize_string('{s}') = '{result}', valid = {is_valid}")
            else:
                status = "✓" if result == expected else "✗"
                if result != expected:
                    all_passed = False
                print(f"Test {i}: {status} reorganize_string('{s}') = '{result}', expected '{expected}'")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

