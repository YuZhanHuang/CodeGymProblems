# Delete Nodes and Return Forest


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def return_forest(root, delete_nodes):
    is_deleted_set = set(delete_nodes)
    forest = []
    
    def dfs(node, is_root):
        if not node:
            return None
        is_deleted = node.data in is_deleted_set
        if is_root and not is_deleted:
            forest.append(node)
        node.left = dfs(node.left, is_deleted)
        node.right = dfs(node.right, is_deleted)
        return None if is_deleted else node
        
    dfs(root, True)
    
    return forest


def tree_to_list(roots):
    """Helper: convert forest to list of root values for testing"""
    return sorted([root.data for root in roots])


# Test cases
if __name__ == "__main__":
    # Test case 1: tree [1,2,3,4,5,6,7], delete = [3,5]
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7
    # After deletion, forest roots: [1, 6, 7]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3, TreeNode(6), TreeNode(7))
    
    # Test case 2: tree [1,2,4,null,3], delete = [3]
    #     1
    #    / \
    #   2   4
    #    \
    #     3
    # After deletion, forest roots: [1]
    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))
    
    test_cases = [
        (root1, [3, 5], [1, 6, 7]),
        (root2, [3], [1]),
    ]
    
    print("Testing Delete Nodes and Return Forest:")
    all_passed = True
    for i, (root, delete_nodes, expected) in enumerate(test_cases, 1):
        result = return_forest(root, delete_nodes)
        result_vals = tree_to_list(result)
        status = "✓" if result_vals == expected else "✗"
        if result_vals != expected:
            all_passed = False
        print(f"Test {i}: {status} return_forest(tree, {delete_nodes}) = {result_vals}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

