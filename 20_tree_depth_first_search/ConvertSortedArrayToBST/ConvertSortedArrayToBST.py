# Convert Sorted Array to Binary Search Tree


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sorted_array_to_bst_helper(nums, low, high):
    if low > high:
        return None
    
    mid = (low + high) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst_helper(nums, low, mid-1)
    root.right = sorted_array_to_bst_helper(nums, mid+1, high)

    return root


def sorted_array_to_bst(nums):
    return sorted_array_to_bst_helper(nums, 0, len(nums)-1)


def is_balanced(root):
    """Check if tree is height-balanced"""
    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
            return -1
        return max(left_h, right_h) + 1
    
    return height(root) != -1


def is_bst(root):
    """Check if tree is a valid BST"""
    def check(node, min_val, max_val):
        if not node:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False
        return check(node.left, min_val, node.data) and check(node.right, node.data, max_val)
    
    return check(root, float('-inf'), float('inf'))


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-10, -3, 0, 5, 9], True),
        ([1, 3], True),
    ]
    
    print("Testing Convert Sorted Array to BST:")
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        root = sorted_array_to_bst(nums)
        is_valid_bst = is_bst(root)
        is_valid_balanced = is_balanced(root)
        result = is_valid_bst and is_valid_balanced
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} sorted_array_to_bst({nums}) -> BST={is_valid_bst}, Balanced={is_valid_balanced}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

