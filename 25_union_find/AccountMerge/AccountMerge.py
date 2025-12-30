# Account Merge

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        root_node1 = self.find(node1)
        root_node2 = self.find(node2)
        if root_node1 != root_node2: 
            self.parents[root_node2] = root_node1


def accounts_merge(accounts):
    n = len(accounts)
    uf = UnionFind(n)
    email_parent = {}
    
    for i, account in enumerate(accounts):
        emails = account[1:]
        
        for email in emails:
            if email in email_parent:
                uf.union(email_parent[email], i)
            email_parent[email] = i
    
    merged_email = defaultdict(list)
    for email, parent in email_parent.items():
        merged_email[uf.find(parent)].append(email)
        
    final_result = []
    for parent, emails in merged_email.items():
        final_result.append([accounts[parent][0]] + sorted(emails))
    
    return final_result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
          ["John", "johnsmith@mail.com", "john00@mail.com"],
          ["Mary", "mary@mail.com"],
          ["John", "johnnybravo@mail.com"]],
         [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
          ["Mary", "mary@mail.com"],
          ["John", "johnnybravo@mail.com"]]),
    ]
    
    print("Testing Account Merge:")
    all_passed = True
    for i, (accounts, expected) in enumerate(test_cases, 1):
        result = accounts_merge(accounts)
        # Sort both for comparison
        result_sorted = sorted([sorted(acc) for acc in result])
        expected_sorted = sorted([sorted(acc) for acc in expected])
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} accounts_merge(...)")
        print(f"  Result: {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

