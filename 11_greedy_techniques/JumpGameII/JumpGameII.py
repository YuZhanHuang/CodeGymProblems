# Jump Game II

def jump_game_two(nums):
    jumps = 0
    farthest = 0
    boundary = 0
    
    for i in range(len(nums)-1):
        farthest = max(farthest, i+nums[i])
        if i == boundary:
            jumps += 1
            boundary = farthest
            
    return jumps


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1], 0),
    ]
    
    print("Testing Jump Game II:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = jump_game_two(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} jump_game_two({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

