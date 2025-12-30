# Basic Calculator


def calculator(s):
    # initialize variable
    number = 0  # current element val
    result = 0  # accumulative result
    sign = 1
    stack = []

    # iterate whole string
    for char in s:
        # is number
        if char.isdigit():
            number = number * 10 + int(char)

        # is operator
        if char in ["+", "-"]:
            result += sign * number
            number = 0
            sign = 1 if char == "+" else -1
        # is (
        elif char == "(":
            stack.append(result)
            stack.append(sign)

            # update current result
            result, sign = 0, 1
        # is )
        elif char == ")":
            result += sign * number
            number = 0
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result

    return result + sign * number


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ]

    print("Testing Basic Calculator:")
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = calculator(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} calculator('{s}') = {result}, expected {expected}")

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")
