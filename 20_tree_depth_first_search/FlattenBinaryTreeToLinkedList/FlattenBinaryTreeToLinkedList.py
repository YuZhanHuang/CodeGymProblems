# Flatten Binary Tree to Linked List


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Solution 1: Using Stack (Preorder Traversal)
def flatten_tree_stack(root):
    if not root:
        return None

    # Stack to keep track of nodes to visit
    stack = []
    stack.append(root)

    prev = None

    while stack:
        # Pop a node from the stack
        current = stack.pop()

        # If we had a previous node, adjust its pointers
        if prev:
            prev.left = None
            prev.right = current

        # Add the right and left children of the current node to the stack
        # We add the right child first so that the left child is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        # Update the previous node to the current node
        prev = current

    return root


# Solution 2: Morris-like Traversal (In-place, O(1) space)
def flatten_tree(root):
    if not root:
        return
    
    current = root
    while current:
        if current.left:
            last = current.left

            while last.right:
                last = last.right
            
            last.right = current.right
            current.right = current.left
            current.left = None

        current = current.right
    return root


# Helper function to print flattened tree
def print_flattened(root):
    result = []
    while root:
        result.append(root.data)
        root = root.right
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,5,3,4,null,6]
    #       1
    #      / \
    #     2   5
    #    / \   \
    #   3   4   6
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(5, None, TreeNode(6))
    
    # Test Stack approach
    flatten_tree_stack(root1)
    result1 = print_flattened(root1)
    expected1 = [1, 2, 3, 4, 5, 6]
    
    # Test case 2 for Morris approach
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root2.right = TreeNode(5, None, TreeNode(6))
    
    flatten_tree(root2)
    result2 = print_flattened(root2)
    
    print("Testing Flatten Binary Tree to Linked List:")
    print(f"Test 1 (Stack): {'✓' if result1 == expected1 else '✗'} {result1}")
    print(f"Test 2 (Morris): {'✓' if result2 == expected1 else '✗'} {result2}")
    
    print("\nAll tests passed!" if result1 == expected1 and result2 == expected1 else "\nSome tests failed!")

