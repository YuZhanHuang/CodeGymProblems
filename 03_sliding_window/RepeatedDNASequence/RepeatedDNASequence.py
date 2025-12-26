# Repeated DNA Sequence


def findRepeatedDnaSequences(s, k):
    to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    encoded_sequence = [to_int[c] for c in s]

    n = len(s)

    if n <= k:
        return []

    a = 4
    h = 0
    seen_hashes, output = set(), set()
    a_k = 1

    for i in range(k):
        h = h * a + encoded_sequence[i]
        a_k *= a

    seen_hashes.add(h)

    for end in range(k, n):
        h = h * a - encoded_sequence[end - k] * a_k + encoded_sequence[end]
        # 要放滾動過的，所以還要再+1
        start = end - k + 1
        if h in seen_hashes:
            output.add(s[start : start + k])
        else:
            seen_hashes.add(h)

    return list(output)


# Driver code
def main():
    # Test case 1: Basic case with repeating sequences
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    k1 = 10
    result1 = set(findRepeatedDnaSequences(s1, k1))
    expected1 = {"AAAAACCCCC", "CCCCCAAAAA"}
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: No repeating sequences
    s2 = "AAAAAAAAAA"
    k2 = 10
    result2 = set(findRepeatedDnaSequences(s2, k2))
    expected2 = set()  # Only one unique sequence
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: String shorter than k
    s3 = "ACGT"
    k3 = 10
    result3 = findRepeatedDnaSequences(s3, k3)
    expected3 = []  # Too short
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Small k value
    s4 = "AAACCCTTTAAA"
    k4 = 3
    result4 = set(findRepeatedDnaSequences(s4, k4))
    expected4 = {"AAA"}  # "AAA" appears multiple times
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: All different sequences
    s5 = "ACGTACGTACGT"
    k5 = 4
    result5 = set(findRepeatedDnaSequences(s5, k5))
    expected5 = {"ACGT", "CGTA", "GTAC", "TACG"}  # Multiple repeating sequences
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
