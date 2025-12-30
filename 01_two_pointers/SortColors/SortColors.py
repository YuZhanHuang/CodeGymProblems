# Sort Colors

def sort_colors(colors):
    RED = 0
    WHITE = 1
    BLUE = 2
    red, white, blue = 0, 0, len(colors) - 1
    
    while white <= blue:
        if colors[white] == RED:
            if colors[red] != RED:
                colors[red], colors[white] = colors[white], colors[red]
            white += 1
            red += 1

        elif colors[white] == WHITE:
            white += 1
        else:
            if colors[blue] != BLUE:
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

    return colors


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),
        ([1, 2, 0], [0, 1, 2]),
        ([2, 2, 2, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 2, 2, 2]),
        ([0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([2, 1, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2]),
    ]
    
    print("Testing Sort Colors:")
    all_passed = True
    for i, (colors, expected) in enumerate(test_cases, 1):
        colors_copy = colors.copy()
        result = sort_colors(colors_copy)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} sort_colors({colors}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

