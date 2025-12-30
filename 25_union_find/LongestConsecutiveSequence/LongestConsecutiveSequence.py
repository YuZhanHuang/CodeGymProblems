# Longest Consecutive Sequence

# Helper class for making connected components 
class UnionFind:
    # Constructor
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}
        self.max_length = 1 if nums else 0

    # Function to find the root of a sequence to which num1 belongs
    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    # Function to merge the two sequences and updating lengths
    def union(self, num1, num2):
        x_root = self.find(num1)
        y_root = self.find(num2)
        if x_root != y_root:
            if self.size[x_root] < self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.max_length = max(self.max_length, self.size[x_root])


def longest_consecutive_sequence(nums):
    # Base Case
    if not nums:
        return 0
    
    # initialize variable
    unique_nums = set(nums)
    mapping = {num: i for i, num in enumerate(unique_nums)}
    uf = UnionFind(unique_nums)
    
    # check connected
    for num in unique_nums:
        if num - 1 in mapping:
            uf.union(num, num-1)
        if num + 1 in mapping:
            uf.union(num, num+1)
    
    # find max
    max_len = 0
    for num in unique_nums:
        root = uf.find(num)
        max_len = max(max_len, uf.size[root])
    
    return max_len


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ]
    
    print("Testing Longest Consecutive Sequence:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = longest_consecutive_sequence(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} longest_consecutive_sequence({nums}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

