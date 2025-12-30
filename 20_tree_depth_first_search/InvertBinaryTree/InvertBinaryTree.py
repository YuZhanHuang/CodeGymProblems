# Invert Binary Tree


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def mirror_binary_tree(root):
    # Base Case
    if root is None:
        return None

    # Recursion 
    left_leaf = mirror_binary_tree(root.left)
    right_leaf = mirror_binary_tree(root.right)

    root.right = left_leaf
    root.left = right_leaf

    return root


def tree_to_list(root):
    """Helper: level-order traversal to list"""
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    #       4              4
    #      / \            / \
    #     2   7    =>    7   2
    #    / \ / \        / \ / \
    #   1  3 6  9      9  6 3  1
    root1 = TreeNode(4)
    root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root1.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    result1 = mirror_binary_tree(root1)
    output1 = tree_to_list(result1)
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    
    # Test case 2: [2,1,3] -> [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    result2 = mirror_binary_tree(root2)
    output2 = tree_to_list(result2)
    expected2 = [2, 3, 1]
    
    print("Testing Invert Binary Tree:")
    print(f"Test 1: {'✓' if output1 == expected1 else '✗'} {output1}")
    print(f"Test 2: {'✓' if output2 == expected2 else '✗'} {output2}")
    
    all_passed = output1 == expected1 and output2 == expected2
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

