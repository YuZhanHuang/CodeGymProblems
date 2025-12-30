# Word Ladder

from collections import deque


def word_ladder(src, dest, words):
    words = set(words)
    if dest not in words:
        return 0

    queue = deque()
    queue.append(src)
    length = 0

    while queue:
        length += 1
        size = len(queue)

        for _ in range(size):
            curr = queue.popleft()

            for i in range(len(curr)):
                alpha = 'abcdefghijklmnopqrstuvwxyz'

                for c in alpha:
                    temp = list(curr)
                    temp[i] = c
                    temp = "".join(temp)

                    if temp == dest:
                        return length + 1

                    if temp in words:
                        queue.append(temp)
                        words.remove(temp)

    return 0


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ]
    
    print("Testing Word Ladder:")
    all_passed = True
    for i, (src, dest, words, expected) in enumerate(test_cases, 1):
        result = word_ladder(src, dest, words.copy())
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} word_ladder('{src}', '{dest}', ...) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

