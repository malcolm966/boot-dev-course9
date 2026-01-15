class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    # 创建一个nil节点
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # 新建一个红节点, 没有任何父子关系
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        # 找到符合BST规则,的插入位置
        # 此节点是最下方节点, 左右节点必然nil
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return
        # 新节点向上建立联系
        new_node.parent = parent
        # 更新父节点的向下联系
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # ?
        self.fix_insert(new_node)

    def fix_insert(self, new_node:RBNode):
        current_node = new_node
        # 如果不是根节点, 并且父亲为红
        # 那么它不能为红
        while (current_node is not self.root 
               and current_node.parent.red):
            # 父亲 爷爷 和uncle
            parent = current_node.parent
            grandparent = parent.parent
            # 如果父亲是右节点
            if(parent is grandparent.right):
                # uncle 是左
                uncle = grandparent.left
                # 如果uncle 红,
                if  uncle.red:
                    # 全部涂黑
                    uncle.red = False
                    parent.red = False
                    # 祖父为红
                    grandparent.red = True
                    current_node = grandparent


                else:
                    if current_node is parent.left:
                        # Move up the tree by making the current node the parent ?
                        current_node = parent
                        self.rotate_right(current_node)
                    parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)

            else:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    # Move up the tree by making the current node the grandparent?
                    current_node = grandparent
                else:
                    if current_node is parent.right:
                        current_node = parent
                        self.rotate_left(current_node)
                    parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False


    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot