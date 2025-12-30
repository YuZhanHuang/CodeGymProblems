# Permutations

def swap_word(word, current_index, i):
    words = list(word)
    words[i], words[current_index] = words[current_index], words[i]
    
    return ''.join(words)


def permute_word_recursive(word, current_index, result):
    if current_index == len(word) - 1:
        result.append(word)
        return

    for i in range(current_index, len(word)):
        word = swap_word(word, current_index, i)
        permute_word_recursive(word, current_index+1, result)


def permute_word(word):
    result = []
    permute_word_recursive(word, 0, result)

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abc", 6),  # 3! = 6 permutations
        ("ab", 2),   # 2! = 2 permutations
        ("a", 1),    # 1! = 1 permutation
    ]
    
    print("Testing Permutations:")
    all_passed = True
    for i, (word, expected_count) in enumerate(test_cases, 1):
        result = permute_word(word)
        status = "✓" if len(result) == expected_count else "✗"
        if len(result) != expected_count:
            all_passed = False
        print(f"Test {i}: {status} permute_word('{word}') has {len(result)} permutations, expected {expected_count}")
        print(f"  Permutations: {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

