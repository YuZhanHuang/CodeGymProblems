# Binary Tree Right Side View


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    result = []
    def dfs(node, level):
        # base case
        if not node:
            return

        if len(result) == level:
            result.append(node.val)

        dfs(node.right, level+1)
        dfs(node.left, level+1)

    dfs(root, 0)
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,null,5,null,4]
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    # Right side view: [1, 3, 4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, None, TreeNode(5))
    root1.right = TreeNode(3, None, TreeNode(4))
    
    # Test case 2: [1,null,3]
    #   1
    #    \
    #     3
    # Right side view: [1, 3]
    root2 = TreeNode(1, None, TreeNode(3))
    
    test_cases = [
        (root1, [1, 3, 4]),
        (root2, [1, 3]),
    ]
    
    print("Testing Binary Tree Right Side View:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = rightSideView(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} rightSideView(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

