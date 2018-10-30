# implementation of Binary Tree


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo


# traverse tree and print pre-order, in-order and post-order
def print_pre_order(tree):
    if tree is None:
        return
    print(tree.cargo, end=" ")
    print_pre_order(tree.left)
    print_pre_order(tree.right)


def print_in_order(tree):
    if tree is None:
        return
    print_in_order(tree.left)
    print(tree.cargo, end=" ")
    print_in_order(tree.right)


def print_post_order(tree):
    if tree is None:
        return
    print_post_order(tree.left)
    print_post_order(tree.right)
    print(tree.cargo, end=" ")


def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)
