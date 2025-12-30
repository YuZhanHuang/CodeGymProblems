# Height of Binary Tree After Subtree Removal Queries

from collections import defaultdict


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def depth_height_rec(node, depth, node_depth, node_height):
    if not node:
        return -1
        
    node_depth[node.data] = depth
    height = max(depth_height_rec(node.left, depth+1, node_depth, node_height), 
                 depth_height_rec(node.right, depth+1, node_depth, node_height)) + 1
    node_height[node.data] = height
    
    return height


def heights_after_queries(root, queries):
    node_depth, node_height = {}, {}
    depth_height_rec(root, 0, node_depth, node_height)
    
    depth_level = defaultdict(list)
    for node, depth in node_depth.items():
        depth_level[depth].append((node_height[node], node))
        depth_level[depth].sort(reverse=True)
        if len(depth_level[depth]) > 2:
            depth_level[depth].pop()
    
    result = []
    for q in queries:
        depth = node_depth[q]
        if len(depth_level[depth]) == 1:
            result.append(depth-1)
        elif depth_level[depth][0][1] == q:
            result.append(depth + depth_level[depth][1][0])
        else:
            result.append(depth + depth_level[depth][0][0])
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: tree [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
    #         1
    #        / \
    #       3   4
    #      /   / \
    #     2   6   5
    #            /
    #           7
    root1 = TreeNode(1)
    root1.left = TreeNode(3, TreeNode(2))
    root1.right = TreeNode(4, TreeNode(6), TreeNode(5, TreeNode(7)))
    
    test_cases = [
        (root1, [4], [2]),
    ]
    
    print("Testing Height After Subtree Removal:")
    all_passed = True
    for i, (root, queries, expected) in enumerate(test_cases, 1):
        result = heights_after_queries(root, queries)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} heights_after_queries(tree, {queries}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

