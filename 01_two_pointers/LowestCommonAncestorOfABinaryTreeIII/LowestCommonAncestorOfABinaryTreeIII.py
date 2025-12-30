# Lowest Common Ancestor of a Binary Tree III

# Definition for a binary tree node with parent pointer
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def lowest_common_ancestor(p, q):
    """
    Walk two pointers up via parent links.  When one pointer
    reaches None, redirect it to the other start.  They will
    meet at the LCA in at most 2·h steps.
    Time: O(h), Space: O(1)
    """
    a, b = p, q
    while a is not b:
        # move up one step, or switch to the other node
        a = a.parent if a else q
        b = b.parent if b else p
    return a


# Helper function to build tree with parent pointers
def build_tree_with_parent():
    """
    Build a test tree:
           3
          / \
         5   1
        / \ / \
       6  2 0  8
         / \
        7   4
    """
    node3 = Node(3)
    node5 = Node(5, parent=node3)
    node1 = Node(1, parent=node3)
    node6 = Node(6, parent=node5)
    node2 = Node(2, parent=node5)
    node0 = Node(0, parent=node1)
    node8 = Node(8, parent=node1)
    node7 = Node(7, parent=node2)
    node4 = Node(4, parent=node2)
    
    node3.left = node5
    node3.right = node1
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8
    node2.left = node7
    node2.right = node4
    
    return {
        3: node3, 5: node5, 1: node1, 6: node6, 2: node2,
        0: node0, 8: node8, 7: node7, 4: node4
    }


# Test cases
if __name__ == "__main__":
    nodes = build_tree_with_parent()
    
    test_cases = [
        (5, 1, 3),  # LCA of 5 and 1 is 3
        (5, 4, 5),  # LCA of 5 and 4 is 5
        (6, 4, 5),  # LCA of 6 and 4 is 5
        (7, 4, 2),  # LCA of 7 and 4 is 2
        (6, 8, 3),  # LCA of 6 and 8 is 3
        (0, 8, 1),  # LCA of 0 and 8 is 1
    ]
    
    print("Testing Lowest Common Ancestor of a Binary Tree III:")
    all_passed = True
    for i, (p_val, q_val, expected_val) in enumerate(test_cases, 1):
        p = nodes[p_val]
        q = nodes[q_val]
        result = lowest_common_ancestor(p, q)
        result_val = result.val if result else None
        status = "✓" if result_val == expected_val else "✗"
        if result_val != expected_val:
            all_passed = False
        print(f"Test {i}: {status} LCA({p_val}, {q_val}) = {result_val}, expected {expected_val}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

