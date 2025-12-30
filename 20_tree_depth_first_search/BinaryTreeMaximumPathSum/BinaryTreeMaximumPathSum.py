# Binary Tree Maximum Path Sum


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def max_path_sum(root):
    max_path = float("-inf")
    
    def max_gain(node):
        nonlocal max_path
        if not node:
            return 0
            
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        whole_path = node.data + left_gain + right_gain
        max_path = max(whole_path, max_path)
        
        return node.data + max(left_gain, right_gain)
    
    max_gain(root)
    return max_path


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3]
    #   1
    #  / \
    # 2   3
    # Max path: 2+1+3 = 6
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    
    # Test case 2: [-10,9,20,null,null,15,7]
    #     -10
    #     / \
    #    9  20
    #      /  \
    #     15   7
    # Max path: 15+20+7 = 42
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    test_cases = [
        (root1, 6),
        (root2, 42),
    ]
    
    print("Testing Binary Tree Maximum Path Sum:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = max_path_sum(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} max_path_sum(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

