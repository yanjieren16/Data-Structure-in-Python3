# thoughts:
#       use Queue to store parent node
#       deQueue parent node and enQueue next level children node

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():

    def __init__(self):
        self.queue = []
        self.list = []

    def breath_first_traversal(self, root):

        if root is None:
            return None
        curr = root
        self.enqueue(curr)
        while self.queue:
            curr = self.dequeue()
            self.list.append(curr.val)
            print("list:", curr.val)
            if curr.left:
                self.enqueue(curr.left)
            if curr.right:
                self.enqueue(curr.right)
        return self.list

    def enqueue(self, node):
        self.queue.insert(0, node)

    def dequeue(self):
        return self.queue.pop()

    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
