import random
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
    # 向左旋转,
    # 拿出该节点的右节点
    def rotate_left(self, pivot_parent:RBNode):
        # 如果当前节点是最外面节点, 停止
        if pivot_parent is self.nil:
            return
        # 如果当前节点的右节点, 是最外面节点, 停止
        if pivot_parent.right is self.nil:
            return
        # 拿出最右面节点当pivot
        pivot = pivot_parent.right
        # 老parent 指向 pivot 的左节点
        pivot_parent.right = pivot.left
        # 如果pivot 的旧 左节点, 不是nil
        # 更新向上指针
        if pivot.left is not self.nil:
            pivot.left.parent = pivot_parent
        # 更新pivot 的向上指针,
        pivot.parent = pivot_parent.parent

        ## 更新向下指针
        # 如果老pivot_parent
        if pivot_parent is self.root:
            self.root = pivot
        elif pivot_parent is pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        elif pivot_parent is pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        # 更新pivot 的向下指针    
        pivot.left = pivot_parent
        # 更新向上指针
        pivot_parent.parent = pivot


    def rotate_right(self, pivot_parent: RBNode):
        if pivot_parent is self.nil:
            return
        if pivot_parent.left is self.nil:
            return

        pivot = pivot_parent.left

        # x 接管 y.right
        pivot_parent.left = pivot.right
        if pivot.right is not self.nil:
            pivot.right.parent = pivot_parent

        # y 接管 x 的父节点
        pivot.parent = pivot_parent.parent
        if pivot_parent is self.root:
            self.root = pivot
        elif pivot_parent is pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot

        # 完成旋转
        pivot.right = pivot_parent
        pivot_parent.parent = pivot


    def insert(self, val):
        # 1. 已val创建一个节点,并默认它为最外面的叶子节点,
        #  所以将它的左右为nil
        new_node = RBNode(val)
        new_node.red = True
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.parent = None

        # 2. Find parent
        parent = None
        current = self.root
        # 如果没有到最外面的nil, 找到合适的插入点
        while current is not self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # Duplicate value
                return

        # 3.Insert new_node, 子节点指向合适的节点
        new_node.parent = parent
        # 4. 父节点向下建立联系
        if parent is None:
            # Tree was empty
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
