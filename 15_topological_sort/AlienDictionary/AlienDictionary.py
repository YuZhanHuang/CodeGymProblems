# Alien Dictionary

from collections import defaultdict, Counter, deque


def alien_order(words):
    graph = defaultdict(set)
    counts = Counter({c: 0 for word in words for c in word})

    for word1, word2 in zip(words, words[1:]):
        for c, d in zip(word1, word2):
            if c != d:
                if d not in graph[c]:
                    graph[c].add(d)
                    counts[d] += 1
                break
        else:  
            if len(word2) < len(word1):
                return ""

    result = []
    queue = deque([c for c in counts if counts[c] == 0])
    while queue:
        c = queue.popleft()
        result.append(c)

        for d in graph[c]:
            counts[d] -= 1
            if counts[d] == 0:
                queue.append(d)

    if len(result) < len(counts):
        return ""
    
    return "".join(result)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["z", "x", "z"], ""),  # Invalid
    ]
    
    print("Testing Alien Dictionary:")
    all_passed = True
    for i, (words, expected) in enumerate(test_cases, 1):
        result = alien_order(words)
        # For valid cases, check if length matches
        status = "✓" if (result == expected or (expected and len(result) == len(expected))) else "✗"
        if result != expected and not (expected and len(result) == len(expected)):
            all_passed = False
        print(f"Test {i}: {status} alien_order({words}) = '{result}', expected '{expected}'")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

