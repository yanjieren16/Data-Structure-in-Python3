# Given an n-ary tree, return the preorder traversal of its nodes' values.
# Definition for a Node.
class TreeNode(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):

    def preorder(self, root):

        list = []
        stack = []

        if root is None:
            return None
        curr = root
        stack.append(curr)
        while stack:
            curr = stack.pop()
            list.append(curr.val)
            print("list:", curr.val)

            while curr.children:
                    stack.append(curr.children.pop())
        return list
