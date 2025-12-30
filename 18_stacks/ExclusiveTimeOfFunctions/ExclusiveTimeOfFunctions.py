# Exclusive Time of Functions

class Log:
    def __init__(self, content):
        content = content.replace(' ', '')
        content = content.split(":")
        self.id = int(content[0])
        self.is_start = content[1] == "start"
        self.time = int(content[2])


def exclusive_time(n, logs):
    result = [0] * n
    stack = []
    for content in logs:
        log = Log(content)
        
        if log.is_start:
            stack.append(log)
        else:
            top = stack.pop()
            result[log.id] += (log.time - top.time + 1)
            if stack:
                result[stack[-1].id] -= (log.time - top.time + 1) 
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"], [3, 4]),
        (1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"], [8]),
        (2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"], [7, 1]),
    ]
    
    print("Testing Exclusive Time of Functions:")
    all_passed = True
    for i, (n, logs, expected) in enumerate(test_cases, 1):
        result = exclusive_time(n, logs)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} exclusive_time(n={n}, logs) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

