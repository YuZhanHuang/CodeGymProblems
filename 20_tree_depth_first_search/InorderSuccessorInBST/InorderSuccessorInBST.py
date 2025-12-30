# Inorder Successor in BST


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_successor(root, p):
    succ = None
    node = root
    while node:
        if p.data < node.data:
            succ = node
            node = node.left
        else:
            node = node.right
        
    return succ


# Test cases
if __name__ == "__main__":
    # Test case 1: BST [2,1,3], p = 1
    #     2
    #    / \
    #   1   3
    # Successor of 1 is 2
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    p1 = root1.left  # node with value 1
    
    # Test case 2: BST [5,3,6,2,4,null,null,1], p = 6
    #         5
    #        / \
    #       3   6
    #      / \
    #     2   4
    #    /
    #   1
    # Successor of 6 is None
    root2 = TreeNode(5)
    root2.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root2.right = TreeNode(6)
    p2 = root2.right  # node with value 6
    
    test_cases = [
        (root1, p1, 2),
        (root2, p2, None),
    ]
    
    print("Testing Inorder Successor in BST:")
    all_passed = True
    for i, (root, p, expected) in enumerate(test_cases, 1):
        result = inorder_successor(root, p)
        result_val = result.data if result else None
        status = "✓" if result_val == expected else "✗"
        if result_val != expected:
            all_passed = False
        print(f"Test {i}: {status} inorder_successor(tree, p={p.data}) = {result_val}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

