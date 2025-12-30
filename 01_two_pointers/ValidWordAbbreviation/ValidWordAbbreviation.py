# Valid Word Abbreviation

def valid_word_abbreviation(word, abbr):
	i, j = 0, 0 

	while i < len(word) and j < len(abbr):
		if abbr[j].isdigit():
			if abbr[j] == '0' and (j == 0 or not abbr[j-1].isdigit()):
				return False
			num = 0
			while j < len(abbr) and abbr[j].isdigit():
				num = num * 10 + int(abbr[j])
				j += 1
			i += num
		else:
			if word[i] != abbr[j]:
				return False
			i += 1
			j += 1

	return i == len(word) and j == len(abbr)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("internationalization", "i12iz4n", True),
        ("apple", "a2e", False),
        ("calendar", "cal3ar", True),
        ("calendar", "c6r", True),
        ("calendar", "c06r", False),  # leading zero
        ("calendar", "cale0ndar", False),  # replaces empty string
        ("word", "word", True),
        ("word", "w2d", True),
        ("word", "4", True),
        ("hi", "2i", False),
        ("hi", "h1", True),
        ("substitution", "s10n", True),
        ("substitution", "sub4u4", True),
        ("substitution", "12", True),
        ("a", "01", False),  # leading zero
    ]
    
    print("Testing Valid Word Abbreviation:")
    all_passed = True
    for i, (word, abbr, expected) in enumerate(test_cases, 1):
        result = valid_word_abbreviation(word, abbr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} valid_word_abbreviation('{word}', '{abbr}') = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

