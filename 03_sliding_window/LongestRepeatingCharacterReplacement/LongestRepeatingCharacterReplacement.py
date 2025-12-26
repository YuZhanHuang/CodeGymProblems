# Longest Repeating Character Replacement


def longest_repeating_character_replacement(s, k):
    start = 0
    most_freq_chr = 0
    chr_dict = {}
    length_of_max_substring = 0

    for end in range(len(s)):
        chr_dict[s[end]] = 1 + chr_dict.get(s[end], 0)
        most_freq_chr = max(most_freq_chr, chr_dict[s[end]])
        curr_win_len = end - start + 1

        if curr_win_len - most_freq_chr > k:
            chr_dict[s[start]] -= 1
            start += 1

        length_of_max_substring = max(end - start + 1, length_of_max_substring)

    return length_of_max_substring


# Driver code
def main():
    # Test case 1: Basic case
    s1 = "ABAB"
    k1 = 2
    result1 = longest_repeating_character_replacement(s1, k1)
    expected1 = 4  # Replace all to "AAAA" or "BBBB"
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: One character dominates
    s2 = "AABABBA"
    k2 = 1
    result2 = longest_repeating_character_replacement(s2, k2)
    expected2 = 4  # "AABA" -> "AAAA"
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: No replacement needed
    s3 = "AAAA"
    k3 = 2
    result3 = longest_repeating_character_replacement(s3, k3)
    expected3 = 4  # Already all same
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: k = 0
    s4 = "ABCDE"
    k4 = 0
    result4 = longest_repeating_character_replacement(s4, k4)
    expected4 = 1  # Can't replace anything
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Complex case
    s5 = "ABAA"
    k5 = 0
    result5 = longest_repeating_character_replacement(s5, k5)
    expected5 = 2  # "AA"
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
