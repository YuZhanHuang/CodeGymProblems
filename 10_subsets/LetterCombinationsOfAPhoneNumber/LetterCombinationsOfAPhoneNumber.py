# Letter Combinations of a Phone Number

def combination_recursive(idx, digits, mapping, path, combinations):
    if len(digits) == len(path):
        combinations.append(''.join(path))
        return
    possible_letters = mapping.get(digits[idx])

    if possible_letters:
        for letter in possible_letters:
            path.append(letter)
            combination_recursive(idx+1, digits, mapping, path, combinations)
            path.pop() 


def letter_combinations(digits):
    if not digits:
        return []

    combinations = []
    path = []
    mapping = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}
    combination_recursive(0, digits, mapping, path, combinations)

    return combinations


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ]
    
    print("Testing Letter Combinations of a Phone Number:")
    all_passed = True
    for i, (digits, expected) in enumerate(test_cases, 1):
        result = letter_combinations(digits)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} letter_combinations('{digits}') = {result}")
        if result != expected:
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

