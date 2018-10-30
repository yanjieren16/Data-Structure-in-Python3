# implementation of Queue


# implementation of linked Queue
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def add(self, cargo):
        node = Node(cargo)

        # if empty, the new node is head and last
        if self.length == 0:
            self.head = node
            self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        # to set last to None when the last node is removed
        if self.length == 0:
            self.last = None
        return cargo

    def is_empty(self):
        return self.length == 0



