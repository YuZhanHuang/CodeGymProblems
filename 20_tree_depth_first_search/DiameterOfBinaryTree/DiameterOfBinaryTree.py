# Diameter of Binary Tree


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def diameter_of_binaryTree(root):
    diameter = 0
  
    def height(node):
        nonlocal diameter
        if not node:
            return 0
            
        lh = height(node.left)
        rh = height(node.right)
        
        diameter = max(diameter, lh + rh)
        
        return max(lh, rh) + 1
        
    height(root)
    
    return diameter


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5]
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # Diameter: 3 (path 4->2->1->3 or 5->2->1->3)
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3)
    
    # Test case 2: [1,2]
    #   1
    #  /
    # 2
    # Diameter: 1
    root2 = TreeNode(1, TreeNode(2))
    
    test_cases = [
        (root1, 3),
        (root2, 1),
    ]
    
    print("Testing Diameter of Binary Tree:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = diameter_of_binaryTree(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} diameter_of_binaryTree(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

