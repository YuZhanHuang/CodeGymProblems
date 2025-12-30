# Restore IP Addresses

def valid(s):
    if len(s) > 3:
        return False

    return int(s) <= 255 if s[0] != '0' else len(s) == 1


def update_segments(s, curr_dot, segments, result):
    segment = s[curr_dot+1:len(s)]

    if valid(segment):
        segments.append(segment)
        result.append('.'.join(segments))
        segments.pop()


def backtrack(s, prev_dot, dots, segments, result):
    size = len(s)

    for curr_dot in range(prev_dot+1, min(prev_dot+4, size-1)):
        segment = s[prev_dot+1:curr_dot+1]

        if valid(segment):
            segments.append(segment)
            if dots - 1 == 0:
                update_segments(s, curr_dot, segments, result)
            else:
                backtrack(s, curr_dot, dots-1, segments, result)
            
            segments.pop()


def restore_ip_addresses(s):
    result = []
    segments = []
    backtrack(s, -1, 3, segments, result)

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ]
    
    print("Testing Restore IP Addresses:")
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = restore_ip_addresses(s)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} restore_ip_addresses('{s}')")
        print(f"  Result: {result_sorted}")
        if result_sorted != expected_sorted:
            print(f"  Expected: {expected_sorted}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

