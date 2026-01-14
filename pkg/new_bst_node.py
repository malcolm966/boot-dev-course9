from user import *
import random

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def get_min(self):
        if self.val is None:
            return None
        if self.left is None:
            return self.val
        else:
            return self.left.get_min()

    def get_max(self):
        if self.val is None:
            return None
        if self.right is None:
            return self.val
        else:
            return self.right.get_max()

    def delete(self, val):
        if self.val is None:
            return None
        elif val < self.val:
            if self.left is not None:
                self.left = self.left.delete()
                return self
            return self
        elif val > self.val:
            if self.right is not None:
                self.right = self.right.delete()
                return self
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        
        successor = self.right.get_min()
        self.val = successor.val
        self.right = self.right.delete(successor.val)
        return self
    
    def preorder(self, visited:list):
        if(self.val is not None):
            visited.append(self.val)
        if(self.left is not None):
            self.left.preorder(visited)
        if(self.right is not None):
            self.right.preorder(visited)
        return visited
    
    def postorder(self, visited:list):
        if(self.left is not None):
            self.left.postorder(visited)
        if(self.right is not None):
            self.right.postorder(visited)
        visited.append(self.val)
        return visited
    
    def inorder(self, visited:list):
        if(self.left is not None):
            self.left.inorder(visited)
        if(self.val is not None):
            visited.append(self.val)
        if(self.right is not None):
            self.right.inorder(visited)
        return visited

    def exists(self, val):
        if(val == self.val):
            return True
        if(val < self.val and self.left is not None):
            return self.left.exists(val)
        if(val > self.val and self.right is not None):
            return self.right.exists(val)
        return False
    

    def height(self):
        if self.val is None:
            return 0
        return max(self.left.height() if self.left is not None else 0, 
                   self.right.height() if self.right is not None else 0) + 1

run_cases = [
    (2, 2),
    (6, 3),
]

submit_cases = run_cases + [
    (0, 0),
    (1, 1),
    (16, 7),
]


def test(num_users, expected_output):
    users = get_users(num_users)
    if not users:
        root = BSTNode()
    else:
        root = BSTNode(users[0])
        for user in users[1:]:
            root.insert(user)

    print("---------------------------------")
    print(f"Users: {[str(user) for user in users]}")
    print_tree(root)
    print(f"Expecting height: {expected_output}")
    result = root.height()
    print(f"Actual height: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()