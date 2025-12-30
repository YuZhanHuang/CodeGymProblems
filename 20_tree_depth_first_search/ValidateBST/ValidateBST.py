# Validate Binary Search Tree

import math


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validate_bst(root):
    prev = [-math.inf]
    return validate_bst_dfs(root, prev)


def validate_bst_dfs(node, prev):
    if not node:
        return True
    
    if not validate_bst_dfs(node.left, prev):
        return False
    # prev node
    if node.data <= prev[0]:
        return False
    prev[0] = node.data

    return validate_bst_dfs(node.right, prev)


# Test cases
if __name__ == "__main__":
    # Test case 1: Valid BST [2,1,3]
    #     2
    #    / \
    #   1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    
    # Test case 2: Invalid BST [5,1,4,null,null,3,6]
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    
    test_cases = [
        (root1, True),
        (root2, False),
    ]
    
    print("Testing Validate BST:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = validate_bst(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} validate_bst(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

