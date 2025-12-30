# Kth Smallest Element in a BST


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def dfs(node, i_order):
    if not node:
        return
    dfs(node.left, i_order)
    i_order.append(node.data)
    dfs(node.right, i_order)
    
    return i_order


def kth_smallest_element(root, k):
    if not root:
        return -1
    i_order = []    
    result = dfs(root, i_order)

    return result[k-1]


# Test cases
if __name__ == "__main__":
    # Test case 1: BST [3,1,4,null,2], k=1
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    # Inorder: [1,2,3,4], k=1 -> 1
    root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    
    # Test case 2: BST [5,3,6,2,4,null,null,1], k=3
    #         5
    #        / \
    #       3   6
    #      / \
    #     2   4
    #    /
    #   1
    # Inorder: [1,2,3,4,5,6], k=3 -> 3
    root2 = TreeNode(5)
    root2.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root2.right = TreeNode(6)
    
    test_cases = [
        (root1, 1, 1),
        (root2, 3, 3),
    ]
    
    print("Testing Kth Smallest Element in BST:")
    all_passed = True
    for i, (root, k, expected) in enumerate(test_cases, 1):
        result = kth_smallest_element(root, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} kth_smallest_element(tree, k={k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

