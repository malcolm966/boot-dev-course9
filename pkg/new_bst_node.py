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
            return
        elif val < self.val:
            if self.left is not None:
                self.left = self.left.delete()
                return self
            return self
        elif val > self.val:
            if self.right is not None:
                self.right = self.right.delete()
                return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        
        successor = self.right.get_min()
        self.val = successor.val
        self.right = self.right.delete(successor.val)
        return self
    
