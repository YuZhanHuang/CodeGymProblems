"""
Linked List helper classes and functions
Reusable data structures for linked list problems
"""

class ListNode:
    """Single node in a linked list"""
    def __init__(self, val=0, next=None, data=None):
        self.val = val if data is None else data
        self.data = val if data is None else data
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def create_linked_list_with_cycle(values, pos):
    """
    Create a linked list with a cycle.
    pos: index where the cycle begins (-1 for no cycle)
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    # Create cycle
    if pos >= 0 and pos < len(nodes):
        current.next = nodes[pos]
    
    return head


def create_circular_linked_list(values):
    """Create a circular linked list (last node points to first)"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    # Make it circular
    current.next = head
    
    return head


def linked_list_to_list(head, max_length=100):
    """Convert linked list to Python list (for non-circular lists)"""
    result = []
    current = head
    count = 0
    
    while current and count < max_length:
        result.append(current.val)
        current = current.next
        count += 1
    
    return result


def circular_linked_list_to_list(head, num_nodes):
    """
    Convert circular linked list to Python list.
    num_nodes: expected number of nodes in the circular list
    """
    if not head:
        return []
    
    result = []
    current = head
    
    for _ in range(num_nodes):
        result.append(current.val)
        current = current.next
    
    return result


def print_linked_list(head, max_length=20):
    """Print linked list for debugging"""
    result = []
    current = head
    count = 0
    
    while current and count < max_length:
        result.append(str(current.val))
        current = current.next
        count += 1
    
    if count == max_length:
        result.append("...")
    
    print(" -> ".join(result))

