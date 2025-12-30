# Verifying an Alien Dictionary

def verify_alien_dictionary(words, order):
    # Build character -> rank map
    rank = {ch: i for i, ch in enumerate(order)}
    
    def in_correct_order(w1, w2):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                return rank[c1] < rank[c2]
        
        return len(w1) <= len(w2)
    
    for i in range(len(words) - 1):
        if not in_correct_order(words[i], words[i+1]):
            return False
    
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    ]
    
    print("Testing Verifying an Alien Dictionary:")
    all_passed = True
    for i, (words, order, expected) in enumerate(test_cases, 1):
        result = verify_alien_dictionary(words, order)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} verify_alien_dictionary({words}, order) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

